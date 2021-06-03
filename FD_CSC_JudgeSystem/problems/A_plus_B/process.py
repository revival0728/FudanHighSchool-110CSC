pre_addr = './problems/A_plus_B/'

def get_args() -> tuple:
    ipt = open(pre_addr+'in1.in', 'r').read()
    ans = open(pre_addr+'out1.out', 'r').read()
    ipt = list(map(int, ipt.strip().split()))
    ans = int(ans.strip())
    return ([ipt], [ans])

def get_file() -> tuple:
    ipt = open(pre_addr+'in1.in', 'r', 100000000)
    ans = open(pre_addr+'out1.out', 'r', 100000000).read()
    return ([ipt], [ans])

def get_limit_time():
    return 5
