'''
terminal judge need get_file() instead get_args()
'''

import default_judge
import subprocess
import importlib
import time
import os
import tkinter as tk

window = tk.Tk()
res = tk.Label(window, text='Result: -')
detail = tk.Toplevel(window)
dres = tk.Label(detail)
code_area = tk.Text(window)
all_problem = []
pid = tk.IntVar()
dinfo = ''
del_show = False

def write_code(code):
    source = open('./user/submit_code.py', 'w')
    source.write(code)
    source.close()

def main():
    write_code(code_area.get('1.0', 'end'))
    result = []
    res.configure(text='Pending')
    problem_id = all_problem[pid.get()]
    problem = importlib.import_module('problems.'+problem_id)
    limit_time = problem.get_limit_time()
    test_in, test_out = problem.get_file() # ([input], [output])
    judge = None
    try:
        judge = problem.judge
    except Exception:
        judge = default_judge.judge
    try:
        for ipt, ans in zip(test_in, test_out):
            popen = subprocess.Popen(['py', './user/submit_code.py'], stdin=ipt, stdout=subprocess.PIPE, encoding='utf-8')
            start = time.monotonic()
            try:
                ret = popen.communicate(timeout=limit_time)[0]
                during = time.monotonic()-start
            except subprocess.TimeoutExpired:
                popen.kill()
                during = limit_time + 0.001
            if during > limit_time:
                result.append(('TLE', during))
                break
            elif judge(ret, ans):
                result.append(('AC', during))
            else:
                result.append(('WA', during))
                break
    except subprocess.CalledProcessError:
        result = [('RE', 0)]
    if not popen.returncode == 0:
        result = [('RE', 0)]
    final_result = result[-1]
    res.configure(text='Result: {}, {:.2f}s'.format(final_result[0], final_result[1]))
    global dinfo
    dinfo = ''
    for i in range(len(result)):
        dinfo += '#{} {}, {:.2f}s\n'.format(i, result[i][0], result[i][1])

def show_detail():
    global del_show
    dres.config(text=dinfo)
    if not del_show:
        detail.deiconify()
    else:
        detail.withdraw()
    del_show = not del_show

def detail_delb():
    dres.config(text='Click the "Detail" again\n')

def GUI():
    #to hiden the console -> save file as [].pyw
    detail.withdraw()
    detail.protocol('WM_DELETE_WINDOW', detail_delb)
    with open('./problems/problem_list.txt', 'r') as f:
        for i in f.readlines():
            all_problem.append(i.strip())
    window.title('Fudan CSC Judge System')
    window.geometry('500x600')
    detail.title('Detail')
    sub_button = tk.Button(window, text='Submit', command=main)
    del_button = tk.Button(window, text='Detail', command=show_detail)
    pick = []
    for i in range(len(all_problem)):
        pick.append(tk.Radiobutton(window, text=all_problem[i], variable=pid, value=i))
    code_area.pack()
    sub_button.pack()
    res.pack()
    del_button.pack()
    for i in pick:
        i.pack()
    dres.pack()

    window.mainloop()

if __name__ == '__main__':
    GUI()
