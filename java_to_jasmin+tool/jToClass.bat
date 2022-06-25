@ECHO off
for %%f in (.\*.*) do java -jar jasmin.jar %%f
java -cp .; D96Class
pause
