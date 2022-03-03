# FDCSC110 Mar4 Handout - Web Crawler II
---

## 複習上一堂課的東西
- [講義連結](https://hackmd.io/@revcoding/fdcsc_110_handouts)

## 本次上課程式碼
- [Github Link](https://github.com/revival0728/FudanHighSchool-110CSC/tree/master/Web_Crawler/for_DDJ)

## 實作環節 - DanDanJudge 的爬蟲
這次我們要爬的是題目的內容，
是一個算簡單，
但是有挑戰性的網站，
很適合拿來練習，
由於時間關係我並不會把所有功能都教一遍，
有興趣的人可以自己去看程式碼。
這次只會爬**題目敘述**、**輸入說明**、**範例輸入**、**範例輸出**、**提示**、**題目名稱**

### Step1 觀察 html
你會發現所有的**題目敘述**、**輸入說明**、**範例輸入**、**範例輸出**、**提示**
都有一個共通點——都是用 `div` 來包裝並且都有 `class="problembox"`，
所以第一步先按照這個規則取出，
接下來只要按照上次教的方法把為文字取出就可以了。
至於**題目名稱**只要把 `<div ... class="h1">` 這個特徵取出就可以了。

### Step2 觀察網址
只要多打開一些題目來觀察，
就可以發現規則如下
```
https://dandanjudge.fdhs.tyc.edu.tw/ShowProblem?problemid=題目的編號
```

### Step3 開始爬蟲
這邊要注意一下，
因為有部分爬蟲適用相同的邏輯來進行操作的，
所以程式碼的部分可能會看起來比較複雜，
要有耐心的去理解。

接下來直接去看程式碼

- [Github Link](https://github.com/revival0728/FudanHighSchool-110CSC/blob/master/Web_Crawler/for_DDJ/simple_version/for_DDJ.py)

有不懂的都歡迎提問

如果不想手動安裝套件的話[點選連結](https://downgit.github.io/#/home?url=https://github.com/revival0728/FudanHighSchool-110CSC/blob/master/Web_Crawler/for_DDJ/requirements.txt)來下載 `requirements.txt`

### Step4 包裝進 `.md` 檔
也就是 `Markdown` 檔，
這裡建議在變成檔案後使用 [HackMd](https://hackmd.io/) 來閱覽。

#### `open()` 使用方法
這個函數有兩種使用方法，
我們這邊教簡單的版本。
使用語法如下
```python
with open([file name], [mode], encoding=[encoding]) as [variable name]:
    ...
```
其中 `mode` 有基本的幾種 `w`、`r`，其他的有點複雜先不講，
`w` 的意思就是 **write** 寫入，
而 `r` 就是 **read** 讀取。
`encoding` 是編碼的意思，可以放入 `Big5`、`utf-8` 等等

如果要寫入文字的話，
可以對 `file object` 使用 `write()` 函數。