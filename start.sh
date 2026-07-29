#!/bin/bash

cd ~/COLLEGE-WEB/backend
nohup uvicorn app.main:app --host 0.0.0.0 --port 8001 > backend.log 2>&1 &

cd ~/COLLEGE-WEB/frontend
nohup npm run dev -- -H 0.0.0.0 -p 3000 > frontend.log 2>&1 &

echo "Backend: http://3.110.85.2:8001"
echo "Frontend: http://3.110.85.2:3000"