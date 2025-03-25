# My CMS
A lightweight CMS with React, Flask, Astro, and MySQL. Create and view blog posts with ease.

## Features
- Signup/login with React  
- Create posts (title, content, images) - authorized only  
- Astro renders posts at `/blogs/`  
- All under `http://localhost:3000`  

## Setup
1. **Clone:**  
   ```bash
   git clone "https://github.com/selvasudar/custom-cms"
2. **Backend:**
    ```bash
    cd backend  
    python -m venv venv  
    source venv/bin/activate  
    pip install -r requirements.txt
3. **Frontend:**
     ```bash
     cd frontend  
     npm install
4. **MySQL:**
    Set up my_cms database (see backend/db.py)
5. Run:
   Use run-all.sh (Unix) or run-all.bat (Windows)

## Usage
-    http://localhost:3000/ → Login/Signup

-    http://localhost:3000/create-post → Create posts
 
-    http://localhost:3000/blogs/ → View posts



