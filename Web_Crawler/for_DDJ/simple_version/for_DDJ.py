#!python3.9

# 建議的測試題目編號 a001, a523, a520

import requests as rqs
from bs4 import BeautifulSoup as bsp

blocks = {  # texts // str
    'title': '',
    'content': '',
    'input': '',
    'output': '',
    'sample_input': '',
    'sample_output': '',
    'hint': '',
    'tag': '',
    'information': '',
    'source': ''
}

url = 'https://dandanjudge.fdhs.tyc.edu.tw/'
pid = 'a001'

def make_md(problem: dict):
    return \
    f'''\
# {problem['title']}
---

## 題目敘述
{problem['content']}
---

## 輸入格式
{problem['input']}
---

## 輸出格式
{problem['output']}
---

## 範例輸入
{problem['sample_input']}
---

## 範例輸出
{problem['sample_output']}
---

## 測資資訊
{problem['information']}
---

## 提示
{problem['hint']}
---

## 題目資訊

### 標籤
{problem['tag']}

### 出處
{problem['source']}
'''

def make_html(innerHTML):
    MathJax_settings = '''\
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {inlineMath: [['$','$']]}
});
</script>
'''
    return f'''\
<!DOCTYPE html>
<head>
<meta charset='utf-8'>
<style>
pre {"{background-color: rgb(217, 217, 217); padding: 10px; border-radius: 3px;}"}
a {"{color: blue;}"}
hr {"{background-color: black;}"}
p {"{font-family: Arial;}"}
h1, h2 {"{font-family: Arial; background-color: rgb(230, 230, 230); padding: 5px; border-radius: 3px;}"}
</style>
{MathJax_settings}
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
</head>
<body>
{innerHTML}
</body>
'''

def process_textp(content, pkeys: list, name: str): # 題目敘述、輸入說明、輸出說明、提示
    pkeys_id = 0
    for id in [0, 1, 2, 5]:
        i = content[id]
        ok = False
        data = i.find_all(name=name)
        if len(data) != 0:
            for j in data:
                img = j.find(name='img')
                if not (img is None):
                    blocks[pkeys[pkeys_id]] += (f"![image]({img.get('src')})" + '\n\n')
                else:
                    blocks[pkeys[pkeys_id]] += (j.text.strip('#') + '\n\n')
                ok = True
        else:
            blocks[pkeys[pkeys_id]] += i.text.strip('#') + '\n\n'
            ok = True

        if ok:
            pkeys_id += 1

def process_textpre(content, pkeys: list, name: str): # 範例輸入、範例輸出
    pkeys_id = 0
    for i in content:
        ok = False
        text = '```\n'
        for j in i.find_all(name=name):
            text_list = j.text.strip().split('\n')
            for t in text_list:
                text += t.strip() + '\n'
            ok = True

        if ok:
            blocks[pkeys[pkeys_id]] += text + '```\n'
            pkeys_id += 1

def process_tag(content): # 標籤
    material = content[-2].find_all(name='a')
    for i in material:
        blocks['tag'] += f"[{i.text}]({url+ i.get('href')[1:].replace(' ', '%')}) "

def process_source(content): # 出處(作者)
    material = content[-1].find_all(name='a')
    if len(material) == 1:
        for i in material:
            blocks['source'] += f"[{i.text}]({url + i.get('href')[1:].replace(' ', '%')})"
    elif len(material) >= 2:
        for i in range(0, len(material)-1):
            blocks['source'] += f"[{material[i].text}]({url + material[i].get('href')[1:].replace(' ', '%')})"
        blocks['source'] += f" authered by [{material[-1].text}]({url + material[-1].get('href')[1:].replace(' ', '%')})"

def process_title(content): # 題目名稱
    material = content.find_all(name='div', attrs={'class', 'h1'})
    blocks['title'] = material[0].text[0:5] + ' ' +material[0].find(name='span').text

def process_information(content): # 測資資訊
    material = content.find_all(name='div', attrs={'class', 'panel-body'})
    info = material[-1].get_text(strip=True).split()
    blocks['information'] += f"```\n{info[0]}{info[1]}MB\n```\n```\n"
    del info[0]
    del info[0]
    for i in range(0, len(info)-1, 5):
        M_index = info[i].find('M')
        if M_index == -1:
            M_index = info[i].find('K')
        if i != 0:
            blocks['information'] += info[i][0:M_index+1] + '\n'
            blocks['information'] += f"{info[i][M_index+1:]} {info[i+1]}{info[i+2]} {info[i+3]}{info[i+4]} "
        else:
            blocks['information'] += f"{info[i][2:]} {info[i+1]}{info[i+2]} {info[i+3]}{info[i+4]} "
    blocks['information'] += info[-1] + '\n```\n\n'

def get_input():
    pid_ipt = input('Please input the problem id: ')
    return 'https://dandanjudge.fdhs.tyc.edu.tw', pid_ipt

def main():

    global url
    global pid
    url, pid = get_input()
    response = None

    try:
        response = rqs.get(f'{url}/ShowProblem?problemid={pid}')
    except Exception:
        response = rqs.get('https://dandanjudge.fdhs.tyc.edu.tw/ShowProblem?problemid=a001')
    html = bsp(response.text, 'html.parser')
    content = html.find_all(name='div', attrs={'class', 'problembox'})

    process_textp(content, ['content', 'input', 'output', 'hint'], 'p')
    process_textpre(content, ['sample_input', 'sample_output'], 'pre')
    process_tag(content)
    process_source(content)
    process_title(html)
    process_information(html)

    for i in blocks:
        if blocks[i].strip() == '':
            blocks[i] = '未提供此資訊\n\n'


    to_html_res = rqs.post('https://api.github.com/markdown', json= {
        'text': make_md(blocks),
        'mode': 'markdown'
    })

    with open('test.html', 'w', encoding='utf-8') as f:
        f.write(make_html(to_html_res.text))

    #with open('test.md', 'w', encoding='utf-8') as f:
    #    f.write(make_md(blocks))

if __name__ == '__main__':
    main()