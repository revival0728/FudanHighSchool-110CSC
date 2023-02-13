# FDCSC110 Sep17 Handout - Hello, Python!

---

## Syntax 語法
`Python` 是一種**強縮排語言**，意思是它的縮排就是它語法的一部份。

`縮排是什麼?`
縮排是把程式碼依照一定的格式用**換行、Tab、Space**來做排版
在**弱縮排語言**中，這個動作只是讓程式碼更好閱讀而已

而 `Python` 是以**Tab**或是**Space**加上**換行**來作為主要縮排語法。
縮排的時機原則上只要上一行的最後一個字元是「:」，就要縮排。

範例程式碼
```python
def main():
    try:
        print(input())
    except EOFError:
        return

if __name__ == '__main__':
    main()
```
在上面的程式碼中，採用**Tab**加上**換行**來縮排，這也是大部分的人的縮排方法。

## Comments 註解
**註解**在程式語言中是不可或缺的一部份，因為當你需要分享你的程式碼，或是程式碼比較複雜時就會需要用到。
而 `Python` 的註解是用 `#` 來表示

範例程式碼
```python
print('hello, world.')    # output "hello, world."
```
很可惜的是 `Python` 沒有多行註解，但可以用多行字串宣告來代替。
```python
print('hello, world.')
'''
This is a Program
that output "hello, world.".
'''
```
## Variables 變數
**變數**，是在程式中儲存數值的方法。
在 `Python` 中，因為是**弱型別語言**，所以不需要宣告變數就可以使用。

範例程式碼
```python
a = 1.0
b = '1.0'
c = 1
print(b)
```
這裡要注意，雖然不需要宣告，但在賦予一個變數值之前，是不能使用的。
```python
print(FDCSC)    # 這是非法的
```

## User Input 輸入
在 `Python` 中，輸入是用 `input()` 函數來達成的。
而 `input()` 函數一次輸入一行，如果要輸入多行，可以用**迴圈**來達成。
這時就會有個問題產生，如果要在一行之內輸入兩個變數時怎麼辦?
這裡的知識就有點超出範圍了，如果不懂的話怎麼辦? ~~背起來就對了~~
基本上，如果有超過一個變數的話要用 `split()`  函數。

範例程式碼
```python
a, b, c = map(int, input().split())    # 輸入 "1 2 3"
print(a+b+c)    # 輸出 6
```

## Boolean 布林值
`Boolean` 其實就是電腦裡面的邏輯，也就是0跟1。
在 `Python` 裡，`True` 代表的是1，`False` 代表的是 0。
在這裡要給大家一個概念，只要一個物件(變數)的值是「0」、「空」等代表**沒有**的概念，
轉換成 `Boolean` 幾乎都是 `False`，反之就是 `True`。

## If..Else 判斷語句

### 邏輯運算
在了解 `判斷語句` 前，必須了解甚麼是程式裡的邏輯。
因為這種語句在寫的時候必須要用邏輯來實現。
下面的表格呈現的是 `True`、`False` 經過邏輯運算子運算後的結果。

`and`運算子
|            |True|False|
|---         |--- |---  |
|**True**    |True|False|
|**False**   |False|False|

`or`運算子
|            |True|False|
|---         |--- |---  |
|**True**    |True|True |
|**False**   |True|False|

`not`運算子
|True|False|
|--- |---  |
|False|True|

範例程式碼
```python
print(True and False)    # False
print(not True)    # False
print(True or False)    # True
```

### 語法
```python
if [Boolean]:
    pass
elif [Boolean]:
    pass
else:
    pass
```

- `if` 是每個判斷句個開頭。只能有一個。
- `elif` 的意思是**else if**，也就是如果還有第二個條件的話，就可以用。可以有**多**個。
- `else` 就是除了 `if`、`elif` 條件以外的東西。只能有一個。
- `pass` 需要再在一個縮排後，沒有程式碼時使用，目的是保持語法的正確性。

範例程式碼
```python
a, b = map(int, input().split())
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print(a+b)
```
在上面的程式碼中，
如果輸入「1 2」會輸出「2」(第五行)
如果輸入「5 3」會輸出「5」(第三行)
如果輸入「4 4」會輸出「8」(第七行)

## Try...Except 偵錯
```python
try:
    pass
except [Exception]:
    pass
finally:
    pass
```
概念跟 `判斷語句` 很像，
只要找到 [Exception]  就執行該 `except` 底下的東西，
如果都沒錯就執行 `try` 底下的東西，
如果有意料之外的錯誤，就執行 `finally` 底下的東西。
其中 [Exception] 可以是 `Exception`、`EOFError`、`TypeError` 等。 
建議要明確找出是哪一種錯誤，不要都用 `Exception`，不然會提高除錯難度。
