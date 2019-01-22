import requests
import re
import random


def get_cookies():
    try:
        # Redirect
        sinaurl = "https://weibo.com/"
        r = requests.get(sinaurl, allow_redirects=False)
        Ugrow_G0 = r.cookies['Ugrow-G0']
        LoginURL = r.headers.get('Location')
        # Get login cookie
        LoginCookie = requests.get(LoginURL).cookies['login']
        # Get tid
        GenURL = "https://passport.weibo.com/visitor/genvisitor"
        Payload = {'cb': 'gen_callback',
                   'fp': {"os": "1", "browser": "Gecko65,0,0,0", "fonts": "undefined", "screenInfo": "1920*1080*24",
                          "plugins": ""}}
        r = requests.post(GenURL, data=Payload, cookies=dict(login=LoginCookie))
        tid = re.search(r'(?<="tid":").*?(?=")', r.text).group(0)
        # Login Again
        LoginURL = "https://passport.weibo.com/visitor/visitor?"
        Payload = {'a': 'incarnate', 't': tid, 'w': '3', 'c': '100', 'gc': '',
                   'cb': 'cross_domain', 'from': 'weibo', '_rand': str(random.uniform(0, 1))+str(random.uniform(999, 10000))}
        r = requests.get(LoginURL, params=Payload, cookies=dict(login=LoginCookie, tid=tid+"__100"))
        sub = r.cookies['SUB']
        subp = r.cookies['SUBP']
        return dict(Ugrow_G0=Ugrow_G0, SUB=sub, SUBP=subp)
    except:
        return {}


def get_cookies_as_visitors():
    cookies = {}
    while not cookies:
        cookies = get_cookies()
    return cookies