#!/usr/bin/python
#-*- coding:utf-8 -*
import re
import requests
import os
import datetime
cur_path = os.path.abspath(os.curdir)



def getPic(html,keyword):


    picture_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    golbal_path = cur_path + '/'+ keyword + '/'
    if not os.path.exists(golbal_path):
        os.mkdir(golbal_path)
    print 'Start downloading images now...'
    for everypic in picture_url:
        print 'downloading'+str(i+1)+'，The url of this picture:'+str(everypic)
        #print(str(datetime.datetime.now()))
        try:
            pic= requests.get(everypic)
        except requests.exceptions.ConnectionError:
            print '【error】Current image cannot be downloaded'
            continue
        except requests.exceptions.Timeout:
            print '【error】timeout'
            continue
        string = golbal_path + keyword+'_'+ str(datetime.datetime.now()) + '.jpg'
	#print (string)
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    input_word = raw_input("Input key word: ")
    urls = ["http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+input_word+"&pn={}".format(str(i)) for i in range(0,81,20)]

    for i in range(len(urls)):
        #print(urls[i])
        re_txt = requests.get(urls[i])
        getPic(re_txt.text,input_word)

