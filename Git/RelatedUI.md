## git gui 操作
1. git bash 鍵入 `git gui &`
2. 等待 UI 介面開啟
3. 介面分成四大塊：
    * 左上為未加入 git 追蹤的檔案、或是已修改過的檔案：Unstaged Changes
    * 左下為加入 git 追蹤的檔案但尚未 commit 的檔案：Staged Changes (Will Commit)
    * 右上為點選任一左上或左下的檔案狀態及內容，需在 local 端修改後 > F5 > 才能看到已更新的內容
    * 右下為進行 commit、push 的位置
4. Unstaged Changes 的檔案於圖標用左鍵點選即可加至 Staged Changes (Will Commit)，反之亦然

## gitk 操作
1. git bash 鍵入 `gitk --all` 或 `gitk --all &`，多加 & 可以避免鎖住 git bash
2. 等待 UI 介面開啟
3. 介面分成三大塊：
    * 上方為 git history 畫面，在文字處點選右鍵可進行 commit、revert 等操作
    * 左下可以看到每個節點前後版本的差異
    * 右下可以看到每個節點牽涉更動的檔案名稱
