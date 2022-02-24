# FDCSC110 Nov19 Handout - Function
---

## Function
程式裡的函數跟數學中的函數有一點不太一樣，
數學中的函數限制較多，
程式中的函數限制較少，
在 `Python` 中更是如此。

### 宣告
```python=
def [Function Name]([Arguments]):
    ...
```

範例程式碼
```python=
def A(x):
    return x**2

def B(x, y):
    return x**y

def C(*args):
    return args[0]**args[1]

def D(**kwargs):
    return kwargs['base']**kwargs['exponent']

def main():
    print(A(2))    # 4
    print(B(3, 2))    # 9
    print(C(2, 4))    # 16
    print(B(y = 9, x = 2))    # 512
    print(D(base = 5, exponent = 2))    # 25
    
if __name__ == '__main__':
    main()
```

### 使用方法

1.
```python=
print(input())
```
上面的程式碼是用來輸出輸入的東西。
`print()` 是一個內建的函數，用於輸出。
`input()` 也是內建函數，用於輸入。
他們分別都有各自的引數，
但只有 `input()` 有回傳，
在數學上可理解為**函數值**，
`print()` 則沒有。

2.
```python=
ar = [i for i in range(1, 11)]
print(sum(ar))    # 55
```
在上面的程式碼中，
有 `sum()` 這個內建函數，
可以看到他以 `ar` 為參數帶入 `sum()` 的引數，
並且回傳 `ar` 裡面所有元素的和。

## Recursion
程式裡的遞迴跟數學的遞迴很像，
但是通常程式裡的遞迴是從末項開始的。
以費氏數列為例，
在數學上的遞迴關係式如下。

$$
fib_n = \begin{cases}
1,\quad n = 1 \\
1,\quad n = 2 \\
fib_{n-1} + fib_{n-2},\quad n > 2 \\
\end{cases}
$$

而在程式上會這樣寫

```python=
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fib(n-1) + fib(n-2)
```

數學上式直接用起始項去推第 $n$ 項，
但程式上是從第 $n$ 出發，找到起始項後再把答案往回做。

其實遞迴的應用很廣，
也很複雜，
像是窮舉、遍歷等，
如果各位有繼續在程式這條路上精進的話，
一定會遇到的。

## List
基本上，
學一個資料結構只要掌握三點就差不多了。
1. 宣告
2. 取值
3. 修改

### 宣告
```python=
a = list()
b = []
```

### 取值
可以用運算子 `[]`
```python=
lst = [1, 2, 'a', 'b', ['c']]

print(lst[1])    # 2
print(lst[4][1])    # 'c'
```

或是迭代一個 `List` 物件
```python=
lst = [1, 2, 'a', 'b', ['c']]

for i in lst:
    if not type(i) == list:
        print(i)
    else:
        for j in i:
            print(j)
```

### 修改
修改可以分成三個部分，
修改值、增加節點、刪除節點。

```python=
lst = [1, 2, 'a', 'b', ['c']]

lst[3] = 'x'
lst.insert(1, 'y')    # 把 'y' 插入到第 1 項
lst.pop()    # 把最後一項刪除
lst.append('z')    # 在最後面加上 'z'
del lst[0]    # 刪除第 0 項
print(lst)    # ['y', 2, 'a', 'x', 'z']

lst.clear()    # 清空整個 List
print(lst)    # []
```
其實還有很多函數，
但是這些其實就夠用了，
如果想要學其他的可以自己去查查看:poop:。

### 合併
其實就把兩個 `List` 相加就好
```python=
lst1, lst2 = [1, 2], ['a', 'b']
lst3 = lst1 + lst2
print(lst3)    # [1, 2, 'a', 'b']
```

### 排序
直接呼叫 `sort()` 函數
```python=
lst = [5, 2, 3, 1, 4]
lst.sort()
print(lst)    # [1, 2, 3, 4, 5]
```
關於 `sort()` 函數其實還有很多可以講，
但因為比較複雜，
這裡就不多作介紹。

## Tuple
可以把它想成不能修改的 `List`，
也就是說 `List` 裡面的**修改**、**排序**它都不能用。
但是他有一個優勢是其他結構無法取代的，
那就是 `unpack`。

```python=
tup = 1, 2, 3

a, b, c = tup
print(a, b, c)    # 1 2 3
```

其實在第一堂課就有遇過他了，
那個當初很毒的輸入又多理解了一項，
那個 `a, b = map(...)`，
`map(...)` 回傳的是 `Map`，
而 `Map` 在被轉成 `Tuple`，
所以才能 `unpack` 給 `a` 跟 `b`。