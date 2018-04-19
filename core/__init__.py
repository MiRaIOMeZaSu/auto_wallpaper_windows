#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from win32api import GetSystemMetrics
from urllib import request
import chardet
from bs4 import BeautifulSoup
import pymysql



User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent


def get_screen_size():
    return [GetSystemMetrics(0), GetSystemMetrics(1)]


def get_html(url):
    try:
        req = request.Request(url, headers=header)
        response = request.urlopen(req)
        html = response.read()
        charset = chardet.detect(html)["encoding"]
        html = html.decode(charset, errors='ignore')
        return html
    except Exception as e:
        print(url)
        print(e)
        return ""


def get_url():
    info = get_screen_size()
    # return "http://image.baidu.com/search/index?ct=&tn=baiduimage&word=%E5%A3%81%E7%BA%B8&pn=0&ie=utf-8&oe=utf-8&cl=&lm=-1&fr=ala&se=&sme=&width="+str(info[0])+"&height="+str(info[1])


def get_bi_an():
    # 获取彼岸壁纸http://www.netbian.com/1920x1080/;http://www.netbian.com/fengjing/
    info = get_screen_size()
    return "http://www.netbian.com/" + str(info[0]) + "x" + str(info[1]) + "/"


def get_agency_ip(html):
    domain = "http://www.netbian.com/"
    soup = BeautifulSoup(html, "lxml")
    # liList = bsObj.findAll("tr", {"class": "odd"})  # 找到所有符合此class属性的li标签
    ips = soup.findAll("div", {"class": "list"})[0].findAll("li")
    list = []
    for x in range(1, len(ips)):
        ip = ips[x]
        tds = ip.findAll("a")
        tds1 = ip.findAll("img")
        domain + tds[0]['href']
        tup = (domain + tds[0]['href'], tds1[0]['src'], tds1[0]['alt'])
        list.append(tup)
    return list


if __name__ == "__main__":
    print(get_agency_ip(get_html("http://www.netbian.com/fengjing/")))
