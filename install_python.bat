@echo off
COLOR A
set /p var="Install Python [1: passive,InstallAllUsers,PerpendPath, 2: quiet,InstallAllUsers,PerpendPath]: "
if %var% == 1 (
cd ".\src\"
start python.exe /passive InstallAllUsers=1 PrependPath=1
echo "Python successfully installed! You can close this windows now."
)
if %var% == 2 (
cd ".\src\"
start python.exe /quiet InstallAllUsers=1 PrependPath=1
echo "Python successfully installed! You can close this windows now."
)
if not %var% == 1 if not %var% == 2 (
echo "Python installation is unsuccessful! Type '1' or '2' on the first page!"
)
exit