# FDCSC110 Dec3 Handout - Math & Operators
---
之所以會想要介紹這個單元是因為 `Python` 最大的用途就是計算!
有很多的經濟、物理、太空等需要大量計算的科系都會使用 `Python` (還有 `Matlab` 啦)

還有探究課也會用到 :poop:
:::spoiler `code`
```python=
import math
import os

sin = math.sin
cos = math.cos
tan = math.tan
arcsin = math.asin
PI = math.pi

C = 16
H = 0
W = 15
deg = 0
L = 25

def deg_to_rad(x):
    return x*PI/180

def rad_to_deg(x):
    return x*180/PI

def calL(x):
    return (H + C*sin(x))*tan(x) + C*cos(x) - W

def calD(x):
    K = L+W
    return arcsin(((4*x*x*C*C-4*(x*x+K*K)*(C*C-K*K))**(1/2)-2*x*C)/(2*(x*x+K*K)))

if __name__ == '__main__':
    while True:
        H, deg = map(float, input('H, deg = ').strip().split())
        print('L = {}cm'.format(calL(deg_to_rad(deg))))
        print('RAD = {}'.format(calD(H)))
        print('DEG = {}'.format(rad_to_deg(calD(H))))
        print('tan(PI/2-x) = {}'.format(tan(PI/2-deg_to_rad(deg))))
    os.system('pause')
```
:::

## Functions from `math`

### 數論衍生函數

#### `ceil(x)`
回傳大於等於 `x` 的最小整數

#### `floor(x)`
回傳小於等於 `x` 的最大整數

#### `comb(n, k)`
回傳 $C_{k}^{n}$

#### `factorial(x)`
回傳 `x` 的階乘

#### `frexp(x, y)`
令 $n = a\times 2^b$，以 `tuple` 回傳 `(a, b)`

#### `ldexp(x, y)`
回傳 $x\times 2^y$，為 `frexp()` 的反函數

#### `fsum(l)`
更精準的計算串列 `l` 裡面的數字總和

#### `gcd(...)`
回傳引數的最大公因數

#### `lcm(...)`
計算引數的最大公因數

#### `nextafter(x, y)`
如果 $x$ 較小回傳 $\lim \limits_{k\to x^{+}} k$，否則回傳 $\lim \limits_{k\to x^{-}} k$

### 指數與對數函數

#### `exp(x)`
回傳 $e^x$

#### `expml(x)`
回傳 $e^x - 1$，比 `exp(x)-1` 精準

#### `log(x, b)`
回傳 $\log_{b} x$，如果 $b$ 沒有參數，則使用預設值 $e$

#### `log1p(x)`
回傳 $\ln (x+1)$，針對 $x$ 趨近於 $0$ 時使用 ($x$ 極小時)

#### `log2(x)`
回傳 $\log_{2} x$，比 `log(x, 2)` 精準

#### `pow(x, y)`
回傳 $x^y$，在 $x=1$ 或 $y=0$ 永遠回傳 $1$，不可計算虛數，以 `float(x)**float(y)` 進行計算

#### `sqrt(x)`
回傳 $\sqrt{x}$，可以使用 `x**0.5`、`pow(x, 0.5)` 取代

### 三角函數

#### `sin(x)`
回傳 $\sin x$

#### `cos(x)`
回傳 $\cos x$

#### `tan(x)`
回傳 $\tan x$

#### `asin(x)`
回傳 $\sin^{-1} x$，回傳值介於 $\frac{\pi}{2}$ 和 $-\frac{\pi}{2}$ 之間

#### `acos(x)`
回傳 $\cos^{-1} x$，回傳值介於 $0$ 和 $\pi$ 之間

#### `atan(x)`
回傳 $\tan^{-1} x$，回傳值介於 $\frac{\pi}{2}$ 和 $-\frac{\pi}{2}$ 之間

#### `atan2(x)`
回傳 $\tan^{-1} x$，回傳值介於 $\pi$ 和 $-\pi$ 之間

### 向量長度衍生函數

#### `dist(x, y)`
`x`、`y` 皆為 `tuple`，回傳 $\lvert \stackrel\longrightarrow{xy} \rvert$

#### `hypot(...)`
令帶入的引數為 $a_1、a_2、...、a_n$，且 $\stackrel\longrightarrow{A} = (a_1, a_2, ..., a_n)$，則回傳 $\lvert \stackrel\longrightarrow{OA} \rvert$

### 角度轉換

#### `degrees(x)`
回傳 `x` 的度度量

#### `radians(x)`
回傳 `x` 的弳度

### 雙曲函數

#### `sinh(x)`
回傳 $\sinh x$

#### `cosh(x)`
回傳 $\cosh x$

#### `tanh(x)`
回傳 $\tanh x$

#### `asinh(x)`
回傳 $\sinh^{-1} x$

#### `acosh(x)`
回傳 $\cosh^{-1} x$

#### `atanh(x)`
回傳 $\tanh^{-1} x$

### 常數
有 $\pi$、$e$。

#### `tau`
相當於 $2\pi$

#### `inf`
相當於 $\infty$

#### `nan`
相當於 `無意義`

## Operators
因為大部分的運算子之前都上過了，
所以這裡著重在**位元運算**。

原則上所有整數 $z$ 都可以被表示為 $\sum \limits_{k=0}^{\infty} a_i\times 2^k$，其中 $a_i\in \{0, 1\}$，
電腦就是以此原則把 $2$ 進位轉換成 $10$ 進位。
舉例 ${10}_{(10)} = {1010}_{(2)}$。
負數的轉換比較複雜，這裡暫時不講

**位元運算子**主要有 $4$ 個，分別是 `&`、`|`、`^`、`~`。

### AND 運算
也就是 `&` 運算，
如果兩個數字取 `&`，
在同一個位元的數字如果其中一個有 $0$，
則該位元就會是 $0$，
反之就會是 $1$。
舉例 `2&1` 會等於 `0`

### OR 運算
也就是 `|` 運算，
如果兩個數字取 `|`，
在同一個位元的數字如果其中一個有 $1$，
則該位元就會是 $1$，
反之就會是 $0$。
舉例 `2&1` 會等於 `3`

### XOR 運算
也就是 `^` 運算，
如果兩個數字取 `^`，
在同一個位元的數字如果值相同
則該位元就會是 $0$，
反之就會是 $1$。
舉例 `2^1` 會等於 `3`

### NOT 運算
也就是 `~` 運算，
一個數字如果取 `~` 運算，
則所有位元反轉。
但是這個會牽扯到負數的位元運算，
所以這裡先不講。

基本上學到這裡已經很後面了，
**位元運算**的主要功能就是省時間，
現在的程式碼還沒有必要用到**位元運算**，
所以有個概念就好。