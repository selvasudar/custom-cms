#!/bin/bash

# Navigate to backend and start Flask
cd backend
source venv/bin/activate  # Activate the Python virtual environment
python app.py &           # Run Flask in the background
FLASK_PID=$!              # Store Flask process ID
cd ..

# Navigate to frontend and start React
cd frontend
npm start &               # Run React in the background
REACT_PID=$!              # Store React process ID
cd ..

# Navigate to astro and start Astro
cd astro
npm run dev &             # Run Astro in the background
ASTRO_PID=$!              # Store Astro process ID
cd ..

# Trap Ctrl+C to kill all background processes
trap "kill $FLASK_PID $REACT_PID $ASTRO_PID; exit" INT

# Wait for all background processes to finish
wait $FLASK_PID $REACT_PID $ASTRO_PID