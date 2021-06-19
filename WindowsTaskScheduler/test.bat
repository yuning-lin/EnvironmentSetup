cd C:\Users\USER\Downloads
virtualenv --python "C:\Users\USER\AppData\Local\Programs\Python\Python37\python.exe" env3.7
fsutil file createnew .\env3.7\Lib\site-packages\a.pth 0
echo %CD% >> .\env3.7\Lib\site-packages\a.pth
call env3.7\Scripts\activate
python GetTime.py

