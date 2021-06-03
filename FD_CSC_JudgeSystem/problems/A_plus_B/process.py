def get_file() -> tuple:
    pre_addr = './problems/A_plus_B/'
    ipt = open(pre_addr+'in1.in', 'r').read()
    ans = open(pre_addr+'out1.out', 'r').read()
    ipt = list(map(int, ipt.strip().split()))
    ans = int(ans.strip())
    return ([ipt], [ans])
    pass

def get_limit_time():
    return 5
