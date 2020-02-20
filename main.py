import requests
from bs4 import BeautifulSoup

def getProxy(num,port=""):
    url = 'http://www.89ip.cn/tqdl.html?num=数量&address=&kill_address=&port=端口&kill_port=&isp='
    url = url.replace("数量",str(num)).replace("端口",str(port))
    r = requests.get(url)
    soup = BeautifulSoup(r.text,features='html.parser')
    s = str(soup.select('div[style="padding-left:20px;"]')[0])
    s=s.replace('<div style="padding-left:20px;">','').replace("</div>","")
    ls = s.split("<br/>")
    ls[0] = ls[0].replace("\n            ","")
    del[ls[-1]]
    f=open("proxies.txt","w")
    for i in range(len(ls)):
        if ls[i] != ls[-1]:
            f.writelines(ls[i]+"\n")
        else:
            f.writelines(ls[i])
    f.close()

if __name__ == "__main__":
    num = input("请输入要提取的数量,最大9999：")
    port = input("请输入要提取的端口，默认随机：")
    getProxy(num,port)

