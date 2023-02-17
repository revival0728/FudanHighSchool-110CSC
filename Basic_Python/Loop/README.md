# FDCSC110 Nov5 Handout - Loop
---

基本上一個比較複雜程式一定要有迴圈才能運作，
也就是說學到這裡算是比較進階的部分了，
因此我希望各位能吸收儘量吸收，
如果不懂的可以等到過幾個月後再回來看。

## While Loop
`while` 迴圈 是 `Python` 裡面最基本的迴圈，
寫起來最簡單，
但比起 `for` 迴圈更容易出現無限迴圈。

### 語法
```python
while [Boolean]:
    ...
```

### 應用

1.
```python
while True:
    print(input())
```
一直輸出輸入進來的東西

2.
```python
i, s = 1, 0
while i <= 10:
    s += i
    i += 1
print(s)    # 55
```
計算 $1$ 到 $10$ 的總和

3.
```python
ar = ['John', 'Tree', 'Han']
i = 0
while i < len(ar):
    print(ar[i])
    i += 1
```
輸出 `ar` 裡面的所有元素

### break and continue
`break` 和 `continue` 都是 `Python` 裡的語法，
功能分別是跳脫迴圈和進行下一次的迴圈

```python
while True:
    n = int(input())
    if n%2 == 0:
        print('{} is even'.format(n))
        break
    else:
        if n == 1:
            continue
        print('{} is odd'.format(n))
```
在上面的程式碼中，
如果輸入 $2$ 則會輸出 "2 is even"，並跳脫迴圈。
如果輸入 $3$ 則會輸出 "3 is odd"。
如果輸入 $1$ 則什麼都不會執行，因為在第 $8$ 行的 `continue`，所以會直接進行下一次的迴圈。

### 練習
[旦旦解題農場-a005: 獨角蟲進化計算器](http://203.64.191.163/ShowProblem?problemid=a005)

`參考解答`
```python
def main():
    w, c, d, ans = 0, 0, 0, 0
    c, w = map(int, input().strip().split())
    while True:
        cnt = c//12
        cnt = min(cnt, w)
        c -= cnt * 12
        d += cnt
        w -= cnt
        c += cnt
        while c < 12 and w > 1 :
            c += 1
            w -= 1
        ans += cnt
        c += d
        d = 0
        if c < 12 or w <= 0:
            break
    print(ans)

if __name__ == '__main__':
    main()
```

## For Loop
`for` 迴圈是所有迴圈裡最不容易出錯的，
因為他的開始和結束都已經規定好了，
除非一開始就放錯，
不然很難出現無限迴圈。

### 語法
```python
for [Variables] in [Iterable Object]:
    ...
```
通常放入 `Iterable Object` 的是 `range`、`list`、`tuple`、`map`、`set`

### 甚麼是 Iterable Object ?
`iterable` 的意思是**可迭代的**。
而迭代的意思是以指針的方式代表資料結構裡的每一個元素，
通常用於遍歷整個資料結構。
而 `iterable object` 的意思就是**可迭代的物件**。

### range 結構
`range` 是 `python` 專門用來迭代的物件，
宣告方式如以下
```python
range([Begin], [End], [Step])
```
上面程式碼的意思是，
宣告一個 `range`，
並且迭代時會從數字**Begin**開始，
直到**End**結束 (不包含**End**)，
且每迭代一次，
所迭代的數字會加上**Step**。

`range` 在只放入一項引數時會判定為**End**，
放入兩項時會判定為**Begin**、**End**。

`enumerate` 也是一個好用的迭代物件，
但因為比較複雜，
也沒有一定要學會，
所以這裡先不講。

### 應用

1.
```python
for i in range(10):
    print(input())
```
輸入 $10$ 次，並且每次都輸出輸入的東西

2.
```python
s = 0
for i in range(1, 11):
    s += i
print(s)    # 55
```
計算 $1$ 到 $10$ 的總和

3.
```python
ar = ['John', 'Tree', 'Han']
for i in ar:
    print(i)
```
輸出 `ar` 裡面的所有元素

`for` 迴圈也有 `break` 和 `continue`

### 練習
[旦旦解題農場-a028: 文文的求婚--續集 (Case 版)](http://203.64.191.163/ShowProblem?problemid=a028)

`參考解答`
```python
def main():
    T = int(input())
    ans = ['a normal year', 'a leap year']

    for case in range(T):
        y = int(input())
        print('Case {}: {}'.format(case+1, ans[y%400==0 or y%4==0 and y%100!=0]))

if __name__ == '__main__':
    main()
```


[旦旦解題農場-a191: Rex 看牙1](http://203.64.191.163/ShowProblem?problemid=a191)

`參考解答`
```python
def main():
    try:
        while True:
            n = int(input())
            
            for i in range(1, n+1):
                for i in range(i):
                    print('%', end='')
                print()

    except EOFError:
        return

if __name__ == '__main__':
    main()
```

## Function
程式裡的函數跟數學中的函數有一點不太一樣，
數學中的函數限制較多，
程式中的函數限制較少，
在 `Python` 中更是如此。

### 宣告
```python
def [Function Name]([Arguments]):
    ...
```

### 使用方法

1.
```python
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
```python
ar = [i for i in range(1, 11)]
print(sum(ar))    # 55
```
在上面的程式碼中，
有 `sum()` 這個內建函數，
可以看到他以 `ar` 為參數帶入 `sum()` 的引數，
並且回傳 `ar` 裡面所有元素的和。
