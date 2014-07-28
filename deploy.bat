call git init
call git add .
call git commit -m "my django app"
call heroku git:remote -a demo-ase --account cuongnm
call git push heroku master
call heroku open --account cuongnm
pause
