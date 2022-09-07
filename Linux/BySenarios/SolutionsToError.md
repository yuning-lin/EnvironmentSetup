## Error1
出現以下錯誤，因為 windows 斷行結尾為 \r\n；linux 斷行結尾為 \n  
所以 linux 會誤認為 \r 為一個字符  
```linux
XXXX.sh: line 1: $'\r': command not found
```
解決方法有二：
* 去除 Script 裡的 \r
```
sed -i 's/\r//' XXXX.sh
```
* 安裝 dos2unix 套件後轉譯
```
yum install -y dos2unix
dos2unix XXXX.sh
```

