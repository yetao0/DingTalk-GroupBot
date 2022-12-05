from doctest import OutputChecker
from tkinter import filedialog
import requests
import time
import hmac
import hashlib
import base64
import urllib.parse
import json
import tkinter
import tkinter.messagebox

#加签
timestamp = str(round(time.time() * 1000))
secret = 'SECd9772fc0564bc073dd0c9192154db623c1c74ad423123e67d47cecdf109ae550'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
url="https://oapi.dingtalk.com/robot/send?access_token=1137e72f5a52a3020b74e6b4b2bea7ef28871672fab46eb3f4dd69c153161c19&timestamp"+timestamp+"&sigh"+sign
print(url)
#GUI
window=tkinter.Tk()
window.title('Dingtalk Bot')
window.geometry('500x500')

title=tkinter.Label(window,anchor="w",text="Ver0.1",justify="center",fg="white",bg="lightblue",font=("TimeNewRoman",30))
text = tkinter.StringVar()


'''def select_file():
    # 单个文件选择
    selected_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
    select_path.set(selected_file_path) 

select_path = tkinter.StringVar()'''

'''tkinter.Label(window, text="文件路径：").grid(column=0, row=0, rowspan=3)
tkinter.Entry(window, textvariable = select_path).grid(column=1, row=0, rowspan=3)
tkinter.Button(window, text="选择单个文件", command=select_file).grid(row=0, column=2)
'''
def got():
    global t
    t=contain.get()
    print (t)
tkinter.Label(window, text="文本消息").grid(column=0, row=0, rowspan=3)
contain=tkinter.Entry(window)
contain.grid(column=1, row=0, rowspan=3)
a=tkinter.Button(window, text='save', width=4,height=1,command=got).grid(column=2, row=0, rowspan=3)
#input


def senta():
    data={
    "msgtype": "link", 
    "link": {
        "text": " 没有训练的一天只好给自己多加几餐啦~嘉心糖们放心喔~吃的很饱睡的很好然后狠狠的让你们想我一下~快说想我！[嘉然2.0_MUA你一下].", 
        "title": "嘉然今天吃什么", 
        "picUrl": "https://i0.hdslb.com/bfs/new_dyn/e8160e55e410f9bd56f38625f5c9d239672328094.jpg@1036w.webp", 
        "messageUrl": "https://t.bilibili.com/734262678472622151"
    }
}
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    data=json.dumps(data)
    x=requests.post(url=url, data=data, headers=HEADERS)
    print(x)
#request

sent = tkinter.Button(window, text='sent', width=4,height=1,command=senta)
sent.place(x = 330,y = 410)
window.mainloop()
