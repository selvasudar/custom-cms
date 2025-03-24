# Custom CMS

A modern Content Management System (CMS) built with React, Python (Flask), Astro, and MySQL. This project enables authorized users to create, manage, and display blog posts with a seamless integration of frontend and backend technologies.

## Features

- **User Authentication**: Secure signup and login using React and Flask with password hashing.
- **Post Creation**: Authorized users can create posts with a title, description, content, feature image, and thumbnail via a React interface.
- **Backend Processing**: Flask handles post details, saves them to MySQL, and generates Astro-compatible Markdown files.
- **Static Frontend**: Astro renders blog posts from Markdown files using frontmatter (title, description, pubDate, heroImage).
- **File Management**: Uploaded images are stored in an `uploads` folder and served by Astro.
- **Authorization**: The `/create-post` route is protected and requires a valid login token.

## Tech Stack

- **Frontend**: React (login, signup, post creation), Astro (static site generation)
- **Backend**: Python (Flask)
- **Database**: MySQL
- **File Storage**: Local `uploads` folder
- **Styling**: Custom CSS for a clean, responsive UI

## Project Structure
my-cms/
├── backend/
│ ├── app.py # Flask backend
│ ├── db.py # MySQL connection
│ └── venv/ # Python virtual environment
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── Login.js # Login page
│ │ │ ├── Signup.js # Signup page
│ │ │ └── CreatePost.js # Post creation page
│ │ ├── App.js # React router setup
│ │ └── styles.css # Shared CSS
│ └── package.json # React dependencies
├── astro/
│ ├── src/
│ │ ├── content/
│ │ │ └── posts/ # Generated Markdown files
│ │ ├── pages/
│ │ │ └── index.astro # Blog post list
│ │ └── content/config.ts # Astro content collection config
│ └── package.json # Astro dependencies
├── uploads/ # Folder for uploaded images
├── run-all.sh # Shell script to run all components (Unix)
├── run-all.bat # Batch file to run all components (Windows)
└── README.md # This file


## Prerequisites

- Python 3.8+
- Node.js 18+ (with npm)
- MySQL 8.0+
- Git

## Setup Instructions

### 1. Clone the Repository

git clone <repository-url>
cd my-cms


### 2. Backend Setup

1. Navigate to the backend directory:
    ```
    cd backend
    ```
2. Set up a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```
    pip install flask flask-cors mysql-connector-python werkzeug
    ```
4. Configure MySQL:
    - Create a database:
      ```
      CREATE DATABASE my_cms;
      ```
    - Update `db.py` with your MySQL credentials:
      ```
      def get_db_connection():
          return mysql.connector.connect(
              host="localhost",
              user="your_username",
              password="your_password",
              database="my_cms"
          )
      ```
5. Run the table creation SQL (see Database Schema section below).

### 3. Frontend Setup

1. Navigate to the frontend directory:
    ```
    cd ../frontend
    ```
2. Install dependencies:
    ```
    npm install
    ```

### 4. Astro Setup

1. Navigate to the Astro directory:
    ```
    cd ../astro
    ```
2. Install dependencies:
    ```
    npm install
    ```

### 5. Environment Configuration

Set a secure `SECRET_KEY` for Flask (optional for JWT in production):

export FLASK_SECRET_KEY="e9b5c8f7a2d3b1e4c5f8d9a0b2e1c3f4d6a7b8e9c0f1d2a3b4e5c6f7d8a9b0e1"

Alternatively, update `app.py` with a hardcoded key for development (not recommended for production).

### 6. Database Schema

Run this SQL in MySQL to create the required tables:

USE my_cms;

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE posts (
id INT AUTO_INCREMENT PRIMARY KEY,
title VARCHAR(255) NOT NULL,
description TEXT,
content TEXT NOT NULL,
feature_image VARCHAR(255),
thumbnail VARCHAR(255),
author_id INT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (author_id) REFERENCES users(id)
);


## Running the Application

### Option 1: Single Command (Unix)

1. Ensure `run-all.sh` is executable:
    ```
    chmod +x run-all.sh
    ```
2. Run:
    ```
    ./run-all.sh
    ```

### Option 2: Single Command (Windows)

Run:
run-all.bat


### Option 3: Manual Start

1. Backend:
    ```
    cd backend && source venv/bin/activate && python app.py
    ```
2. Frontend:
    ```
    cd frontend && npm start
    ```
3. Astro:
    ```
    cd astro && npm run dev
    ```

## Usage

- **Signup**: Visit `http://localhost:3000/signup` to create an account.
- **Login**: Go to `http://localhost:3000/` to log in.
- **Create Post**: After logging in, navigate to `http://localhost:3000/create-post` to create a post.
- **View Posts**: Open `http://localhost:4321` (Astro) to see the rendered blog posts.

## Endpoints

- `POST /api/signup`: Register a new user (`username`, `email`, `password`).
- `POST /api/login`: Log in and receive a token (`username`, `password`).
- `POST /api/posts`: Create a post (requires Authorization header with token).

## Security Notes

- Tokens are currently stored in-memory (`VALID_TOKENS`). Use JWT and a database like Redis in production.
- Keep the `SECRET_KEY` secure and unique per environment.
- Deploy with HTTPS in production.

## Future Improvements

- Implement JWT for robust token management.
- Add logout functionality.
- Use cloud storage services (e.g., AWS S3) for uploaded files.
- Enhance UI with a CSS framework like Tailwind CSS.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests to improve the project.

## License

This project is licensed under the MIT License.

---
