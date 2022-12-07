import os
import urllib2
def command():
    result= os.popen("命令").read()
    return result

url_code = urllib2.quote(command())

url="bark服务器网址+设备码"+url_code+"?level=passive" #例如 http://server/yourkey/ 替换
req=urllib2.Request(url)
resp=urllib2.urlopen(req)
data=resp.read().decode('utf-8')
print(data)
