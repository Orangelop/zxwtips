@echo off
COLOR A
set /p var="Install pip module - zhixuewang [1: change pip mirror & install, 2: only install]: "
if %var% == 1 (
cmd /k "pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple & pip install zhixuewang"
echo "pip module - zhixuewang successfully installed! You can close this windows now."
)
if %var% == 2 (
cmd /c "pip install zhixuewang"
echo "pip module - zhixuewang successfully installed! You can close this windows now."
)
if not %var% == 1 if not %var% == 2 (
echo "pip module - zhixuewang installation is unsuccessful! Type '1' or '2' on the first page!"
)
pause