# My CMS
A lightweight CMS with React, Flask, Astro, and MySQL. Create and view blog posts with ease.

## Features
- Signup/login with React
- Create posts (title, content, images) - authorized only
- Astro renders posts at /blogs/
- All under http://localhost:3000

## Setup
Clone: git clone "https://github.com/selvasudar/custom-cms"
Backend: cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
Frontend: cd frontend && npm install
MySQL: Set up my_cms database (see backend/db.py)
Run: Use run-all.sh (Unix) or run-all.bat (Windows)

## Usage
http://localhost:3000/ - Login/Signup
http://localhost:3000/create-post - Create posts
http://localhost:3000/blogs/ - View posts

## Tech
React (frontend)
Flask (backend + proxy)
Astro (static blogs)
MySQL (database)

## Notes
Set FLASK_SECRET_KEY env var for security.
Rebuild Astro after new posts: cd astro && npm run build && mv dist/* ../backend/static/blogs/
