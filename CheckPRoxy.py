#!/usr/bin/python
import os,  time, requests, sys, threading

def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])

cls()




def xx(PROXY, url):
    try:
        sess = requests.session()
        sess.proxies = {'http': PROXY}
        sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        aa = sess.get('http://' + url, timeout=5, proxies={'http': PROXY})
        if aa.status_code == 200:
            print PROXY + '   GooD'
            with open('OKproxy.txt', 'a') as xX:
                xX.write(PROXY + '\n')
        else:
            print PROXY + '   BaD'
    except:
        print PROXY + '   BaD'


def main():
    try:
        fileproxy = sys.argv[1]
        url = sys.argv[2]
    except:
        print '  [-] Usage : python CheckPRoxy.py proxylist.txt target'
        sys.exit()
    if url.startswith("http://"):
        url = url.replace("http://", "")
    elif url.startswith("https://"):
        url = url.replace("https://", "")
    else:
        pass
    with open(fileproxy, 'r') as x:
        prox = x.read().splitlines()
    thread = []
    for proxy in prox:
        t = threading.Thread(target=xx, args=(proxy, url))
        t.start()
        thread.append(t)
        time.sleep(0.02)
    for j in thread:
        j.join()

main()



