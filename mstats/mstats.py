# coding: utf-8

import requests
import datetime
import pytz

urls = ['http://qt.gtimg.cn/q=bkqtRank_A_sh',
'http://qt.gtimg.cn/q=bkqtRank_A_sz']


def getStatsInfo(url):
    try:
        rest = requests.get(url)
        rst = rest.text
        infos = rst.split('=')[1].replace('"', '').split('~')
        up = int(infos[2])
        sideway = int(infos[3])
        down = int(infos[4])
        print (up,sideway,down,(1*(up)+0*(sideway)+(-1)*(down))/(float(up)+float(sideway)+float(down)))
    except Exception as e:
        print "Error:[%s]" % e

def main():
    print datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    for url in urls:
        getStatsInfo(url)

if __name__ == '__main__':
    main()






