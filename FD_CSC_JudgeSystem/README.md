# FD_CSC_JudgeSystem
A simple Python judge system for judging output/return_value is correct or not.

## How to use it
You just need paste your solution to the textbox then click "submit"

If you want to see result of every substack then click "Detail"

The judgement will stop if your answer is wrong or finishes juding all the substack

Below is the probable result of this system

- **TLE**: Time Limit Exceed
- **RE** : Runtime Error
- **WA** : Wrong Answer
- **AC** : Accept

## Add a problem
Add a module in "problems" folder

If you want to use "function judge" then the module needs to contain function **get_args** and **get_limit_time**

If you want to use "terminal judge" then the module needs to contain function **get_file** and **get_limit_time**

All the system above needs to add your problem name (module name) in "problem_list.txt"

Below is the example of the **get_args**, **get_limit_time**, and **get_file** function

```python
def get_args() -> tuple:    # ([str], [str])
    ipt = open(pre_addr+'in1.in', 'r').read()
    ans = open(pre_addr+'out1.out', 'r').read()
    ipt = list(map(int, ipt.strip().split()))
    ans = int(ans.strip())
    return ([ipt], [ans])    # ([input1, ...], [answer1, ...])

def get_file() -> tuple:    # ([file], [str])
    ipt = open(pre_addr+'in1.in', 'r', 100000000)
    ans = open(pre_addr+'out1.out', 'r', 100000000).read()
    return ([ipt], [ans])    # ([input1, ...], [answer1, ...])

def get_limit_time() -> float:
    return 5    # second
```

You can also code your own judge function

Just add **judge** function in your module

Below is the example of the **judge** function

```python
def judge(ret, ans) -> bool:
    ret = ret.replace(' ', '')
    ret = ret.replace('\n', '')
    ret = ret.replace('\r', '')
    ans = ans.replace(' ', '')
    ans = ans.replace('\n', '')
    ans = ans.replace('\r', '')
    return ret == ans
```