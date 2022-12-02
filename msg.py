#!python3
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
# python get-pip.py
# pip install pypushdeer 

import os
import sys
import re
from pypushdeer import PushDeer   #pip install pypushdeer

unknow = []
sent = []
recv = []

def get_msg_num(line):
    return int(line.rstrip(' (sent)\n').rstrip(' (received)\n').rstrip(' (unknown)\n')[::-1].split('/',1)[0][::-1])

def send_msg(num):
    os.system("mmcli -s "+str(num)+" --send")

def del_msg(num):
    os.system("mmcli -m 0 --messaging-delete-sms="+str(num))

def scan_local_msg():
    p=os.popen('mmcli -m 0 --messaging-list-sms') 
    for line in p.readlines():
        if line.endswith(' (unknown)\n'):
            num = get_msg_num(line)
            unknow.append(num)
        if line.endswith(' (sent)\n'):
            num = get_msg_num(line)
            sent.append(num)
        if line.endswith(' (received)\n'):
            num = get_msg_num(line)
            recv.append(num)    
    print('未发送：',unknow,'已发送：',sent,'接收：',recv)

def add_msg(number,text):
    os.system("mmcli -m 0 --messaging-create-sms=\"text=\'"+text+"\',number=\'+"+number+"\'\"")

def clean_sent():
    for i in sent:
        del_msg(i)
        
def clean_unknow():
    for i in unknow:
        del_msg(i)
        
def clean_recv():
    for i in recv:
        del_msg(i)

def send_all():
    for i in unknow:
        send_msg(i)

def forward_msg():
    for i in recv:
        p=os.popen('mmcli -m 0 -s '+str(i))
        #delete '\s|\t|\n|-' 删除特殊字符
        sms=re.sub('\s|\t|\n|-','',p.read())
        #get number 查找并输出
        number=sms[sms.find('number:')+7:sms.find('|text')]
        #get text 查找并输出
        text=sms[sms.find('text:')+5:sms.find('Properties|')]
        #get time 查找并输出再替换
        time=sms[sms.find('timestamp:')+10:sms.find('timestamp:')+27].replace('T',' - ')
        # pushdeer = PushDeer(server="server:8800", pushkey="key") # 自建pushdeer推送服务器 修改pushkey
        pushdeer = PushDeer(pushkey="pushkey")  # 默认服务器 修改pushkey
        pushdeer.send_text(number+'\n'+text+'\n\n'+time)


cmd = sys.argv
cmd_len = len(cmd)

if cmd[1] == 'help':
    print('随身wifi短信转发')
    print('Command: help add send clean forward')
elif cmd[1] == 'add':
    add_msg(cmd[2],cmd[3])
elif cmd[1] == 'send':
    scan_local_msg()
    send_all()
elif cmd[1] == 'clean':
    scan_local_msg()
    clean_sent()
    clean_unknow()
    clean_recv()
elif cmd[1] == 'forward':
    scan_local_msg()
    forward_msg()
else:
    print('Command error.')
