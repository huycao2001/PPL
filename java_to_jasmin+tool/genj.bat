@ECHO off
del /Q bin\*.class
del /Q jasmin\*.j
javac -d bin test.java
for %%f in (bin\*.*) do java -cp bcel-5.2.jar JasminVisitor.java %%f
move /y *.j jasmin
for %%f in (jasmin\*.*) do java -jar jasmin.jar %%f
move /y *.class bin
java -cp bin test
pause
