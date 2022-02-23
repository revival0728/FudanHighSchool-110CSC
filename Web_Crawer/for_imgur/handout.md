# FDCSC110 Feb25 Handout - Web Crawer I
---

## 複習上學期的東西
- [講義連結](https://hackmd.io/@revcoding/fdcsc_110_handouts)

## 本次上課範例程式碼
- [Github Link](https://github.com/revival0728/FudanHighSchool-110CSC/tree/master/Web_Crawer/for_imgur)

## 物件導向 (OOP)
只要開始實作一些比較大型的程式時，
就一定會用到的觀念，
甚至一些遊戲引擎把 **OOP** 設定成基本架構，
例如 `Unity`、`Godot` 等。
用簡單一點的方式來解釋的話，
就是把相關的變數、函數打包成一個物件，
這樣做的好處有很多，
例如 **避免重名**、**方便維護** 等。
以下我們來看個範例。

今天要記錄每位學生的段考成績，
需要紀錄的資訊有 **姓名**、**學號**、**數學成績** 和 **自然成績**，
如果不使用 **OOP** 的程式碼如下
```python=
name = ['John', 'Tree', 'Hank']
ID = ['911001', '911002', '911003']
math_score = [100, 95, 90]
science_score = [90, 95, 100]
```
這樣的程式碼乍看之下還可以，
但是等到實際操作時會非常不直覺，
因為會是用索引值來操作，
其實這個方法可以用 `dict` 來解決
```python=
scores = {
    'John': {
        'ID': '911001',
        'math_score' = 100
        'science_score' = 90
    },
    ...
}
```
這樣操作起來會好很多，
因為是用生活中的名詞來取值，
但是有一個缺點——不易宣告，
這個辦法也很好解決，
寫一個打包函數就好了。
```python=
def score_packer(ID: str, math_score: int, science_score: int):
    return {
        'ID': ID,
        'math_score': math_score,
        'science_score', science_score
    }
```
以上看到的一連串變化就是 **OOP** 的前身，
其實只要把打包函數、`dict` 包進一個 `class` 裡面就完成 **OOP** 的實現了。
```python=
class score:
    def __init__(self, name: str, ID: str, math_score: int, science_score: int):
        self.name = name
        self.ID = ID
        self.math_score = math_score
        self.science_score = science_score
        
scores = [
    score('John', '911001', 100, 90),
    score('Tree', '911002', 95, 95),
    score('Hank', '911003', 90, 100)
]
```
這學期的程式碼都會有 **OOP** 版本的，
想要學的可以去看看。

## requests
這是 `Python` 一個很適合用於爬蟲的套件，
因為篇幅我們只講會用到的東西，
想要研究的可以[點選連結](https://docs.python-requests.org/en/latest/)去自習。

### 匯入模組
```python=
import requests as rqs
```

### get()
```python=
response = rqs.get('https://imgur.com/search?q=hololive')
```
這個函數會回傳造訪網頁的所有結果，
爬蟲只會用到裡面的 `.text` 也就是 `html`

## bs4 - BeautifulSoup
這是 `Python` 裡面用來分析大量字串的套件，
一樣很適合用於爬蟲，
想要更深入研究的可以[點選連結](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### 匯入模組
```python=
from bs4 import BeautifulSoup as bsp
```

### 宣告
```python=
html = bsp(html_text, 'html.parser')
```

### find_all(name, attrs, recursive, string, **kwargs)
```python=
element = html.find_all(name='div', attrs={'class', 'cards'})
```
這個函數很重要，
幾乎就是整個爬蟲的靈魂，
這次會用到的只有引數 `name` 和 `attrs` 而已。
`name` 抓的就是 `html` 中的元素類型
`attrs` 抓的就是每個元素裡面的資料，像是 `class`、`color`、`type`、`id`、`data` 等
由於是找出所有符合的結果，
所以會回傳 `list`，
只要數一下你要的元素在第幾個就好。

## Pillow - Image
這個是用來顯示圖片的模組，
是這次實作特別需要用到的，
跟爬蟲無關，
想要深入學習的請[點選連結](https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=image)

### 匯入模組
```python=
from PIL import Image
```

### 宣告
```python=
image = image.open(res_pic.raw)
```

### show()
```python=
image.show()
```
這個函數是用來把圖片顯示到畫面的，
等等實作時會就會理解了，
不過有個缺點是只要開啟了，
就沒辦法用程式關閉，
因為主導權已經轉移給作業系統了。

## 實作環節 - imgur.com 的爬蟲
這次需要用到的新東西非常少，
希望各位能好好的學起來，
做出來的東西蠻酷的。

眾所周知，
`imgur` 是一個充滿圖(好)片(香)的網站，
因此只要能把圖片爬出來，
就相當於掌握了整個網站。

### Step1 觀察 html
打開 `imgur` 後搜尋 `hololive`，
對圖片選右鍵後打開檢查頁面，
右邊就會出現 `html`，
你會發現承裝圖片的元素為 `img`，
而他的母元素是一個 `div`，
一個 `div` 代表的就是一個圖片，
再往上找我們會發現再上面這個 `div` 裝著所有圖片，
我們的目標就是用 `BeautifulSoup` 把它找出來。

### Step2 觀察網址
想爬蟲，
首先一定要有網址，
這個網址的規律很好看出來，
```
https://imgur.com/search/?q=想要查的內容
```
如果有空白，
就用 `+` 取代。

### Step3 開始爬蟲
這邊就直接看程式碼就好了，
- [Github Link](https://github.com/revival0728/FudanHighSchool-110CSC/blob/master/Web_Crawer/for_imgur/simple_version/for_imgur.py)
有不懂的都歡迎提問