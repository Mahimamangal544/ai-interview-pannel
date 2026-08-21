@REM ----------------------------------------------------------------------------
@REM Maven Wrapper startup batch script
@REM ----------------------------------------------------------------------------
@echo off
setlocal

set MAVEN_WRAPPER_JAR="%~dp0\.mvn\wrapper\maven-wrapper.jar"
set MAVEN_WRAPPER_PROPERTIES="%~dp0\.mvn\wrapper\maven-wrapper.properties"

for /F "usebackq tokens=1,2 delims==" %%a in (%MAVEN_WRAPPER_PROPERTIES%) do (
    if "%%a"=="distributionUrl" set DISTRIBUTION_URL=%%b
)

if not exist "%~dp0\.mvn\wrapper\maven-wrapper.jar" (
    echo Downloading Maven Wrapper jar...
    java -jar "%~dp0\.mvn\wrapper\maven-wrapper.jar" %*
) else (
    java -jar "%MAVEN_WRAPPER_JAR%" %*
)
endlocal
