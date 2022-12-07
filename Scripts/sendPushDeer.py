#!python3
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
# python get-pip.py
# pip install pypushdeer 
import os
from pypushdeer import PushDeer   #pip install pypushdeer

def command():
    result= os.popen("命令").read()
    return result

# pushdeer = PushDeer(server="server:8800", pushkey="key") # 自建pushdeer推送服务器 修改pushkey
pushdeer = PushDeer(pushkey="pushkey")  # 默认服务器 修改pushkey
pushdeer.send_text(command())
