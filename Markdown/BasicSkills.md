## 簡介
README.md：以個人的淺見就是簡述整個 project 或資料夾的概要  
其中 .md 其實就是 markdown 的縮寫  
markdown 本身是利用純文字編寫就可以轉換成 html 文件的語法  
利用簡單的標記，讓文件整體可以更清晰易讀  
以下內文僅呈現在 github 上相容的 markdown 語法做整理介紹  
## 標題
文字前的 # 數目越少顯示的字體越大
```
# 最大
## 次之
### 次次之
#### 次次次之
##### 次次次次之
###### 次次次次次之
```
# 最大
## 次之
### 次次之
#### 次次次之
##### 次次次次之
###### 次次次次次之

## 引言
大於符號＋一個空白鍵：框住引言，多個＞帶有巢狀形式  
ENTER 鍵：自動生成大於符號
```
> When there is a will there's a way.
> > 有志者事竟成
```
> When there is a will there's a way.
> > 有志者事竟成

## 分隔線
四個星號組成分隔線
```
****
```
****

## 文字編輯
語法|呈現
----|----
`  ` |行尾兩個空白鍵做斷行
`*斜體*` |*斜體*
`**粗體**` |**粗體**
`~~刪除線~~` |~~刪除線~~
`<ins>底線</ins>` |<ins>底線</ins>

## 數學公式
用錢字號括住 Latex 語法  
Latex 語法詳參：http://www.cs.nthu.edu.tw/~cherung/teaching/2009cs5321/link/latex.pdf
```
傅立葉變換公式：$f(t)=\int_{-\infty}^\infty f(t) e^{-iwt}dt$ 
```
傅立葉變換公式：$f(t)=\int_{-\infty}^\infty f(t) e^{-iwt}dt$ 

## 清單列表
### 無序標號
星號＋一個空白鍵：即可生成列表  
ENTER 鍵：自動生成下列，行尾無須再加上兩個空白鍵  
tab 鍵：生成下一個階層
```
* 第一層
  * 第二層
    * 第三層 
```
* 第一層
  * 第二層
    * 第三層 
### 有序標號
數字＋.＋一個空白鍵：即可生成有序列表   
ENTER 鍵：自動生成加項序列  
兩個 tab 鍵：生成下一個階層的有序列表  
有序標號和無序標號可以交互使用  
```
1. 主序列一
2. 主序列二
    1. 次序列一
    2. 次序列二
```
1. 主序列一
2. 主序列二
    1. 次序列一
    2. 次序列二
### 清單（check list）
減號＋一個空白鍵＋中括號：建立待辦事項  
若是中括號為一個空白鍵：未勾選  
若是中括號為一個小 x：有勾選
```
- [ ] 沒打勾  
- [x] 有打勾 
```
- [ ] 沒打勾  
- [x] 有打勾  

## 內嵌程式
下列反引號為鍵盤上數字 1 旁的 \`  
### 顯示行內區塊：\`程式碼\`    
```
    印出 `print()`
```
印出 `print()`

### 顯示多行區塊：\`\`\`程式碼\`\`\`
```
    ```
    def ChangePosition(a,b):
      a, b = b, a
      return a, b
    ```
```
```
def ChangePosition(a,b):
  a, b = b, a
  return a, b
```

### 顯示該程式語法高亮：\`\`\`python 程式碼\`\`\` 
```
    ```python
    def ChangePosition(a,b):
      a, b = b, a
      return a, b
    ```
```
```python
def ChangePosition(a,b):
  a, b = b, a
  return a, b
```

### 利用＋－！＃將匡列區塊顯示文字顏色
```
    ```diff  
    + 綠色 green
    - 紅色 red
    ! 橘色 orange
    # 灰色 grey
    ```
```
```diff  
+ 綠色 green
- 紅色 red
! 橘色 orange
# 灰色 grey
```
## 建立表格
利用至少三個減號＋豎線做表頭和資料的區隔  
利用冒號呈現文字置中、置右的效果；若無冒號預設置左
```
序號|語法|呈現
----:|:----:|----
1|`  ` |行尾兩個空白鍵做斷行
2|`*斜體*` |*斜體*
3|`**粗體**` |**粗體**
4|`~~刪除線~~` |~~刪除線~~
5|`<ins>底線</ins>` |<ins>底線</ins>   
```
序號|語法|呈現
----:|:----:|----
1|`  ` |行尾兩個空白鍵做斷行
2|`*斜體*` |*斜體*
3|`**粗體**` |**粗體**
4|`~~刪除線~~` |~~刪除線~~
5|`<ins>底線</ins>` |<ins>底線</ins>    

## 引用網址
### 另行命名網址
```
[yuning-lin's github](https://github.com/yuning-lin)
```
[yuning-lin's github](https://github.com/yuning-lin)
### 直接貼上網址
```
https://github.com/yuning-lin
```
https://github.com/yuning-lin

## 嵌入圖片
1. 將圖片上傳至 github 某處
2. 右鍵複製連結網址
3. `![圖片參考定義](網址)`
```
![upload files](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/github_UploadFile.png)
```
![upload files](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/github_UploadFile.png)
