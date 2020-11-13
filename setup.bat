@echo off

set LIB_PATH=%1
set UPGRADE=

if "%LIB_PATH%"=="" (
    set LIB_PATH=.\Lib\site-packages
    set UPGRADE=--upgrade
)

setlocal EnableDelayedExpansion

cd /d %~dp0
Set MAYA_MODULE_PATH=%cd%;%MAYA_MODULE_PATH%

set MAYA_APP_PATH=null

for /l %%v in (2030, -1, 2015) do (
    FOR /F "TOKENS=1,2,*" %%I IN ('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\%%v\Setup\InstallPath" /v "MAYA_INSTALL_LOCATION"') DO IF "%%I"=="MAYA_INSTALL_LOCATION" SET MAYA_APP_PATH=%%K

    if not !MAYA_APP_PATH!==null goto install_pip
)

goto except

:install_pip
set MAYAPY_PATH="%MAYA_APP_PATH%bin\mayapy.exe"

call %MAYAPY_PATH% -m pip

if not %errorlevel%==0 (
    curl https://bootstrap.pypa.io/get-pip.py | %MAYAPY_PATH%
)

call %MAYAPY_PATH% -m pip install --upgrade pip

call %MAYAPY_PATH% -m pip install %UPGRADE% -r requirements.txt -t %LIB_PATH% --use-feature=2020-resolver

goto end

:except
echo Maya is not installed.
pause

:end
pause
