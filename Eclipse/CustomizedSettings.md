## Code Style
#### 選擇 Code Formatter
1. Window > Preferences > PyDev > Editor > Code Style > Code Formatter
2. 選擇 autopep8（default 段行字數：79）
3. 若想要改變設置：
    * 改變斷行長度為 150 字：可在 `Parameters for autopep8` 後方空白格處輸入 `--max-line-length=150`
    * 免除斷行預設為 79 字：可在 `Parameters for autopep8` 後方空白格處輸入 `--ignore E501`
4. Apply and Close

#### 套用 Code Formatter
* Window > Preferences > PyDev > Editor > Save Actions > 勾選 `Auto-format editor contents before saving`
* 如此可以在修改後按儲存時自動套用格式

#### 檢視當前程式是否符合 Code Formatter 設置
* 診斷是否符合 autopep8 設置：project > 右鍵 > PyDev > Code Analysis
* 快捷鍵使用 autopep8 斷行：`ctrl+shift+f`
* 不符設定的程式碼會在行頭顯示 `!`，修正後儲存即可

## 個人化顯示
* 改變顯示符號：General > Editors > Text Editors
  * 顯示程式碼行號：勾選 `Show line numbers`
  * 顯示換行符號等：勾選 `Show whitespace characters`
* 調整字型、字體、大小：General > Appearence > Colors and Fonts
  * 調整程式碼字體：Basic > Text Font > 點選 Edit
  * 調整左側專案樹狀字體：View and Editor Folder > Tree and table font for views
  * 調整檔案點開 banner 字體：View and Editor Folder > Part title font

## 改變主題背景
* 簡易更換：General > 點選 Appearence > Theme 選 `Dark`
* 更多選擇：
  1. Help > Install New Software > Add
      * Name 輸入：Eclipse Color Theme
      * Location 輸入：http://eclipse-color-theme.github.io/update/
        
      ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/eclipse_install_color_theme.PNG)
        
  2. Add > Select All > Next > Accept the terms of the license agreement > Finish
  3. Select All > Trust Selected > Restart Now
        
      ![](https://github.com/yuning-lin/EnvironmentSetup/blob/main/SetUpPic/eclipse_trust.PNG)
        
  4. Window > Preferences > General > Appearance > Color Theme
  5. 選擇喜愛的主題或是點選 `Import a theme` 引入喜愛的主題
