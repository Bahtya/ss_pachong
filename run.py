import requests
import base64
import re

headers ={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie':'__cfduid=dcb472bad94316522ad55151de6879acc1479632720; locale=en; _ga=GA1.2.1575445427.1479632759; _gat=1; _hjIncludedInSample=1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
path = './ss.png'
filename = 'ss.png'
def pic_dl():
    pic= requests.get('https://freess.cx/images/servers/jp02.png',headers=headers)
    fp = open(path,'wb')  
    fp.write(pic.content)  
    fp.close() 

def pic_upload():
    url='http://jiema.wwei.cn/fileupload.html?op=jiema&token=2142df115ef9acb957830725d09b8246ef6291a8'
    files={'file':open(path,'rb'),'filename':filename}
    #files={'file':requests.get('https://freess.cx/images/servers/jp02.png').content}
    res=requests.post(url,files=files)
    res = res.json()
    result= (res['data'])
    result=base64.b64decode(result)
    #print (result)
    reg = r'aes.*?n:[0-9][0-9][0-9][0-9][0-9]'
    m=re.findall(reg,str(result))
    print('源代码:'+m[0])

pic_dl()
pic_upload()
