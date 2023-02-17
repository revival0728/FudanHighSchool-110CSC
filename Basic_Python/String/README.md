# FDCSC110 Oct22 Handout - String
---

## Data Types

### 變數類型
- **Text Type**: `str`
- **Numberic Types**: `int`, `float`, `complex`
- **Sequence Types**: `list`, `tuple`, `range`
- **Mapping Type**: `dict`
- **Set Types**: `set`, `frozenset`
- **Boolean Type**: `bool`
- **Binary Types**: `bytes`, `bytearray`, `memoryview`

### 宣告方法
可以直接設值，讓編譯器自己判斷。
```python
x = "Hello World"    # str	
x = 10    # int	
x = 10.5    # float	
x = 1j    # complex	
x = ["Fudan", "Computer", "Science"]    # list	
x = ("Fudan", "Computer", "Science")    # tuple	
x = range(10)    # range	
x = {"Club" : "FDCSC", "Ranking" : 1}    # dict	
x = {"Fudan", "Computer", "Science"}    # set	
x = frozenset({"Fudan", "Computer", "Science"})    # frozenset	
x = True    # bool	
x = b"Hello"    # bytes	
x = bytearray(10)    # bytearray	
x = memoryview(bytes(10))    # memoryview
```
或者是可以直接用 `class` 的**建構元**。
這裡舉幾個例子
```python
x = str("Hello World")    # str
x = int(10)    # int
x = dict(Club="FDCSC", Ranking=1)
```
剩下的就依此類推，把**資料結構**的名稱加上()裡面放入需要的**引數**就可以了。

## Numbers
**Number Type**有 `int`、`float`、`complex`。

### int
就是**整數**的意思，在 `Python` 中，所有的整數預設都是用 `int` 儲存的。
`int` 支援的運算子有 `+`、`-`、`*`、`/`、`//`、`**`、`%`、`>`、`<`、`==` 等運算子。

### float
就是**浮點數**的意思，比較熟悉的講法是**小數**，所有的小數預設都是用 `float` 儲存的。
`float` 支援的運算子有 `+`、`-`、`*`、`/`、`//`、`**`、`%`、`>`、`<`、`==` 等運算子。

### complex
這個可能比較不熟悉一點，在數學上這是**複數**。
**複數**，是數系中範圍最廣的，包含了**實數**和**虛數**。
`複數 = 實部 + 虛部`，而在 `Python` 中一個複數可以表示為 `"float" + "float + j"` (例如:`1+2j`)
`float` 支援的運算子有 `+`、`-`、`*`、`/`、`**`、`>`、`<`、`==` 等運算子。

## Strings
`str`，也就是字串，是一個非常重要的東西，可以說是本節課的重點。
講到這裡應該都知道怎麼宣告了，就直接進到用法。

### 取值
`str` 可以取出字串中特定的字元，或是特定的一段子字串。

範例程式碼
```python
s = 'FDCSC'

print(s[0])    # 'F'
print(s[2:5])    # 'CSC'
```
在上面的程式碼中，
`s[0]` 代表的是取出第**1**個字元，
`s[2:5]` 代表的是取出第**2~4**個字元。

### 修改
由於可以修改 `str` 的函數很多，這裡就講一些比較常用的。

範例程式碼
```python
s = 'FDCSC'

s[0] = 'D'    # s = 'DDCSC'
s = ' ABCKINGDOM    '.strip()    # s = 'ABCKINGDOM'
s = s.replace('ABC', 'DD')    # s = 'DDKINGDOM'
s = s + 'GG'    # s = 'DDKINGDOMGG'
s = 'Ranking: {}, Score: {:.2f}'.format(1, 99.9999)    # s = 'Ranking: 1, Score: 100'
s = 'Ranking: {}, Score: {:.3f}'.format(1, 99.9949)    # s = 'Ranking: 1, Score: 99.995'
s = '{}*{}={}'.format(1, 2, 1*2)    # s = '1*2=2'
s = 2*s    # s = '1*2=21*2=2'
s = 3*'a'    # s = 'aaa'
```
- **LINE: 3**: 把第一個字元設為 `'D'`
- **LINE: 4**: 所有的 `'ABC'` 變成 `'DD'`
- **LINE: 5**: 在字串的末端加上 `'GG'`
- **LINE: 6**: `format()` 的用意是把字串中 `{}` 依序改變成**引數**的值，而 `{:.2f}` 代表的是四捨五入到小數點後第 2 位
- **LINE: 7**: 同**LINE: 6**，但是變成四捨五入到小數點後第 3 位
- **LINE: 8**: 同**LINE: 6**
- **LINE: 9**: 這個等同於 `s+s` 也就是把 `'1*2=2'` 的末端再加上一個 `'1*2=2'`
- **LINE: 10**: 這行就是把 `s` 設為 3 個 `'a'`

### 其他輔助函數
這裡介紹幾個好用的輔助函數

```python
a = 'a123a'
b = '123'
c = 'aa'
e = '(2**2 + 3/2 + 100%4)%17'
r = '1 a b cde 3.5'

print(a.isdecimal())    # False
print(b.isdecimal())    # Talse
print(c.isdecimal())    # False

print(a.isalpha())    # False
print(b.isalpha())    # False
print(c.isalpha())    # Talse

print(eval(e))    # 5.5
print(r.split())    # ['1', 'a', 'b', 'cde', '3.5']
print(e.find('3/'))    # 8
print(e.count('2'))    # 3
print(len(a))    # 5
```
- `isdecimal()` 是用來判斷字串裡的字元是否全部都是數字
- `isalpha()` 是用來判斷字串裡的字元是否全部都是字母
- `eval()` 是用來執行字串中的程式碼
- `split()` 把字串中以空白分開的字元視為一個變數，並且存進一個 `list` 裡面
- `find()` 是用來找出第一個在字串中出現的連續子字串，並回傳他的 `index` (索引值)
- `count()` 是用來數一個連續子字串出現過幾次
- `len()` 會回傳字串的長度

## Scope
一個變數可以依據他宣告的地方不同而分成**全域變數**和**區域變數**。
下面就用範例程式碼來講解

```python
n, m = 1, 2

def add():
    a, b = n, m
    return a+b

print(add())    # 3
```
在上面的程式碼中，
`n`、`m` 是屬於**全域變數**，
`a`、`b` 是屬於 `add()` 函數 的**區域變數**。
**全域變數**的意思就是在這個程式碼的任何地方都可以使用的變數，
**區域變數**就是只能在特定區域使用的變數，
例如 `a`、`b` 為 `add()` 函數中的**區域變數**，
所以 `a`、`b` 只能在 `add()` 函數中使用。

另外在宣告前面加上 `global` 就會讓那個變數宣告成**全域變數**。
```python
n, m = 1, 2

def add():
    global a, b
    a, b = n, m
    return a+b

print(add())    # 3
```
在上面的程式碼中 `a`、`b` 為**全域變數**

## Map

現在我們要來拆解第一次上課的程式碼了，
還記得下面這行毒瘤嗎?
```python
m, n = map(int, input().split())
```
現在你應該除了 `map()` 函數都要看的懂了。
其實 `map()` 就是把 `input().split()` 回傳的 `list` 的每一項執行**引數1**的函數，
而我們帶入的是 `int()`，所以這行程式碼的意思就是
> 把輸入拆解成 `list` 之後，把每一項轉換成 `int`，並且在轉換成 `tuple`，最後把前兩個變數分別存入 `n`、`m`。

這句話如果現在不懂沒關係，等你寫久了會慢慢懂得:poop:。
題外話，如果輸入超過 1 個空白，`Python` 會出現 `Exception`，並且終止程式。
