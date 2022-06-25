@ECHO off
for %%f in (jasmin\*.*) do java -jar jasmin.jar %%f
move /y *.class bin
java -cp bin test
pause
