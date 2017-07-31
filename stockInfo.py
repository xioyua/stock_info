import win32api
import win32con
import os
import time

class win32Doc:
    _public_methods_ = ['write']
    def write(self,s):
        print(s)

import urllib
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import gzip
import lxml
import sys

class login_web:

    eleName = ["股票名字","今日开盘价","昨日收盘价","当前价格","今日最高价","今日最低价","竞买价",\
"竞卖价","成交的股票数","成交金额","买一n","买一p","买二n","买二p","买三n","买三p","买四n",\
"买四p","买五n","买五p","卖一n","卖一p","卖二n","卖二p","卖三n,","卖三p","卖四n","卖四p","卖五n","卖五p","日期","时间"]

    def __init__(self):
        '''设置头，cookie'''
        self.players = []
        self.opener = urllib.request.build_opener()
        user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101"
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        connection = "keep-alive"
        host = "10.189.37.35:7100"
        upgrade = "1"
        headers = {'User-Agent': user_agent,
                   'Accept': accept,
                   'Connection': connection,
                   'Host': host,
                   'Upgrade-Insecure-Requests': upgrade,
                   }
        header = []
        for key, value in headers.items():
            elem = (key, value)
            header.append(elem)
        print(header)
        self.opener.addheaders = header

    def ungzip(self, data):
        try:  # 尝试解压
            data = gzip.decompress(data).decode()
        except:
            print('未经压缩, 无需解压')
        return data

    def getInfo(self,id):
        '''从people页面获得第一批用户信息，通过扫描关注列表，得到大量用户信息'''
        url = "http://hq.sinajs.cn/list=" + id
        try:
            request = urllib.request.Request(url)
            response = self.opener.open(url)
            html = response.read().decode('gb2312')
            #html = self.ungzip(html)
            #print(html)
            self.dealInfo(html)
            #soup = BeautifulSoup(html, 'lxml')
        except urllib.error.URLError as e:
            print(e.reason)
            print("有错误")
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)

    def dealInfo(self,info):
        if info:
            element = info.split(',')
            self.dic = {}
            i = 0
            for each in self.eleName:
                self.dic [each] = element[i]
                i += 1
            self.dic['股票名字'] = self.dic ['股票名字'].split('"')[1]
id = input("please input a number\n")
hi_price = float(input("请输入你想要提醒的上限价格\n"))
lo_price = float(input("请输入你想要提醒的下限价格\n"))
lg = login_web()
while True:
    lg.getInfo(id)
    print(lg.dic['股票名字']+':'+lg.dic['时间']+' : ' +  lg.dic['当前价格'])
    if float(lg.dic['当前价格']) >= hi_price or float(lg.dic['当前价格']<=lo_price):
        win32api.MessageBox(0, str(lg.dic['当前价格'])+'价格已达到', "注意啦", win32con.MB_ICONWARNING)
        break
    time.sleep(5)

