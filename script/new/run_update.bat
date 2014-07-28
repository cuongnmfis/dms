rem set "mongo_path=C:\data\db\mongo"
rem set mongo_path = "D:\App\mongodb\bin\mongo.exe"
set "mongo_path=C:\mongodb\bin"
set "script=C:\mongodb\script"

call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\remove.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\category.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\progresstype.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\impression.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\unit.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\mentor.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\student.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\curriculumn.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\action.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\materialtype.js"
pause
call "%mongo_path%\mongo.exe" oceanic.mongohq.com:10043/my_db -u admin -p 113322 "%script%\material.js"
pause

