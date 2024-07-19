@echo off
cd ./content/post
git add .
git commit -m "Post"
git push origin main
cd ..
timeout /t 2
exit
