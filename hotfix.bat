@echo off
COLOR A
set dir=%ProgramFiles%\Python310\lib\site-packages\zhixuewang\student
set origin=%cd%
echo [+] Quick Hotfix for zhixuewang PIP Module, fit for python 3.10 amd64 installed for all users
set /p var="[+] Will move "%cd%\hotfix\student.py" to "%dir%" and create a backup. [1: install]: "
if %var% == 1 (
echo [+] Create backup
pushd "%dir%"
ren student.py student.py.BACKUP
echo [+] Copy hotfix
pushd %origin%
copy "%cd%\hotfix\student.py" "%dir%"
)
pause