from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from db import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from datetime import datetime
import secrets
import mysql 
import datetime

# current_time = datetime.datetime.now()

app = Flask(__name__)
# CORS(app)  # Enable CORS for React
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

UPLOAD_FOLDER = '../astro/public'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SECRET_KEY = secrets.token_hex(32)

# In-memory token store (for simplicity; use a database in production)
VALID_TOKENS = {}

# Signup endpoint
@app.route('/api/signup', methods=['POST'])
def signup():
    print(request.method)
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Use the correct hashing method
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, email)
            VALUES (%s, %s, %s)
        """, (username, hashed_password, email))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "User created successfully"}), 201

    except mysql.connector.Error as err:
        return jsonify({"message": f"Error: {str(err)}"}), 400

# Update login endpoint to use hashed passwords
from werkzeug.security import check_password_hash

@app.route('/api/check', methods=['POST'])
def hello():
    print("selva")
    return jsonify({"message": "Login successful", "user_id": 'id'}), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (data['username'],))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user['password'], data['password']):
        return jsonify({"message": "Login successful", "user_id": user['id']}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Middleware to check authorization token
def check_auth():
    token = request.headers.get('Authorization')
    user_id = request.form.get('user_id')  # Get user_id from the form data
    if not token or not user_id or token != VALID_TOKENS.get(int(user_id)):
        return False
    return True

# Create post endpoint
@app.route('/api/posts', methods=['POST'])
def create_post():
    # if not check_auth():
        # return jsonify({"message": "Unauthorized"}), 401

    title = request.form['title']
    description = request.form['description']
    content = request.form['content']
    author_id = request.form['user_id']

    # Handle file uploads
    feature_image = request.files.get('feature_image')
    thumbnail = request.files.get('thumbnail')
    feature_path = thumbnail_path = None

    if feature_image:
        feature_path = os.path.join(app.config['UPLOAD_FOLDER'], feature_image.filename)
        feature_image.save(feature_path)
    if thumbnail:
        thumbnail_path = os.path.join(app.config['UPLOAD_FOLDER'], thumbnail.filename)
        thumbnail.save(thumbnail_path)

    # Save to MySQL
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO posts (title, description, content, feature_image, thumbnail, author_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, description, content, feature_path, thumbnail_path, author_id))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    # Generate Markdown file with Astro-compatible frontmatter
    current_date = datetime.datetime.now().strftime('%b %d %Y')  # e.g., "Mar 24 2025"
    # hero_image_path = f'/{feature_path}' if feature_path else '/blog-placeholder-4.jpg'
    hero_image_filename = os.path.basename(feature_path) if feature_path else 'blog-placeholder-4.jpg'
    md_content = f"""---
title: '{title}'
description: '{description}'
pubDate: '{current_date}'
heroImage: '/{hero_image_filename}'
---

{content}
"""

    # Write the Markdown file
    md_file_path = f"../astro/src/content/blog/post_{post_id}.md"
    with open(md_file_path, "w") as f:
        f.write(md_content)

    return jsonify({"message": "Post created", "post_id": post_id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)