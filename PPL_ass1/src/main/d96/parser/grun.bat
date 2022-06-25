@ECHO OFF
SET TEST_CURRENT_DIR=%CLASSPATH:.;=%
if "%TEST_CURRENT_DIR%" == "%CLASSPATH%" ( SET CLASSPATH=.;%CLASSPATH% )
@ECHO ON
java -cp ".;C:\Javalib\antlr-4.9.2-complete.jar" org.antlr.v4.runtime.misc.TestRig %*