rem set "mongo_path=C:\data\db\mongo"
rem set mongo_path = "D:\App\mongodb\bin\mongo.exe"
set "mongo_path=C:\data\db"
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\usertype.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\workfeild.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\jobtitle.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\userprofile.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\mentorpost.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%cd%\commentpost.js"