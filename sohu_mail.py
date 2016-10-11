#coding=utf-8
#!/usr/bin/python

import requests
import fileinput

url="http://sendcloud.sohu.com/webapi/mail.send.json"

HtmlFile = "/Users/mac/Documents/summer/py/index.html"
AddressFile = "/Users/mac/Documents/summer/py/me.list"

#stradd = ''
for eachline in fileinput.input(AddressFile):
    address = eachline.split( );

    fo = open(HtmlFile, "rb")
    str = fo.read();
    str = str.replace('wing',address[0])
    fo.close()

#add = open("E:/SendMail/add.txt", "rb")
#stradd = add.read();
  
# 不同于登录SendCloud站点的帐号，您需要登录后台创建发信子帐号，使用子帐号和密码才可以进行邮件的发送。
    params = {"api_user": "Mail_pl", \
        "api_key" : "Wj3iH7TLScHy1s",\
        "to" : address[1], \
        "from" : "noreply@service.com", \
        "fromname" : "4477", \
        "subject" : "精品推荐第九期", \
        "html": str \
    }

    try:
        r = requests.post(url, files={}, data=params)
        print r.text
    catch Exception, ex:
        pass


#add.close()