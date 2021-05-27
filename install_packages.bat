@echo off


:start
cls

set python_ver=36

python ./get-pip.py

cd \
cd \python%python_ver%\Scripts\
py -m pip install -U pygame --user
py -m pip install -U openpyxl --user

pause
exit