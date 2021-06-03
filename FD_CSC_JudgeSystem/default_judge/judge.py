def judge(ret, ans) -> bool:
    ret = ret.replace(' ', '')
    ret = ret.replace('\n', '')
    ret = ret.replace('\r', '')
    ans = ans.replace(' ', '')
    ans = ans.replace('\n', '')
    ans = ans.replace('\r', '')
    return ret == ans