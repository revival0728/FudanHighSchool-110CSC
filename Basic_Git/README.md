# FDCSC110 Apr1 Handout - Basic Git
---

## 甚麼是 Git
**git** 是一種版本管理的概念，
主要用於程式碼的協作。

## 為什麼需要 Git
因為每位工程師分配到的程式碼不同，
完成的時間也不一樣，
所以需要有東西來幫忙**合併**每個人寫的程式碼。

## Git 的基本概念
可以把每次上傳的程式碼當作一個分枝，
上傳後的程式碼會被自動合併到當前的主分枝。
而會有一些人是專門審查程式碼的，
在大致看過程式碼的合理性後，
他們會將程式碼**合併**到整個專案的主分枝。

舉個例子
今天tree、rev、Hank 三個人在協作一個DanDanJudge的爬蟲，
tree負責寫前端互動，
rev負責寫爬蟲主程式，
Hank負責寫網頁架構。
顯然這三個工作是完全可以分開做的，
因此在協作的過程中，
他們只要將程式碼分別傳到自己的分枝上 (tree、rev、Hank)，
最後在由其中一人合併就可以了。

## Git 指令
有很多指令，
這邊只教平常會用到的，
更詳細的教學可以[點擊這裡](https://git-scm.com/docs/git)

### git branch
這是用來管理本地分枝的指令

#### 新增分枝
```console
git branch <branch-name>
```

#### 新增並切換分枝
```console
git branch -b <branch-name>
```

#### 切換分枝
```console
git checkout <branch-name>
```

### git add
這是用來將更變提交至本地的**git**

```console
git add <file-name>
git add .
```

如果參數是`.`的話，代表將所有更變提交。

### git commit
這是用來將本地更變提交打包的指令

```console
git commit -m "<message>"
```

每次的打包一定要包含一串字串來敘述的這次的變更。

### git push
這是用來將打包提交至雲端的指令

```console
git push <remote> <branch>
```

將`remote` 上的分枝 `branch` 上傳。 (通常 `remote` 都是 `origin`)

### git pull
這是用來將雲端程式碼合併至本地的指令

```console
git pull origin
```

因為 `pull` 真的不常用，所以這裡指講合併自己的專案就好。

### git clone
這是用來將雲端專案複製到本地的指令

```console
git clone <repository-url>
```

在複製時有很多種網址格式可以用，
最常看到的有 `https` 和 `ssh`，
`https` 在每次上傳時都要輸出帳密 (如果我沒記錯的話)，
因此很少人用，
事實上 `Github` 已經宣布停止支援用 `https` 上船程式碼 (下載還是可以的)，
而 `ssh` 因為本身自帶金鑰，
所以不需要再輸入帳密，
只需要在帳號設定一次即可，
是比較常見的方法。
如果想要學 `ssh` 的可以來找我 (~~我會查給你看~~)。

## 常見的 Git 雲端
有各位已經有的[Github](https://github.com/)、[Bitbucket](https://bitbucket.org/)、[Gitlab](https://gitlab.com/) 等等，我自己是用 `Github`。

## 小結
雖然 `git` 在程式碼協作時很好用，
但在一個人實作專案時也是一個很好用的工具，
畢竟他的是**版本管理器**，
在程式出現嚴重bug時要復原還是很好用的。

最後提一下，
這個講義沒有講到如何解決`Merge Conflict`，
解決辦法非常簡單，
自己查一下就有了，
但樣成好習慣，
在寫之前記得先 `pull` 就可以避免了。


