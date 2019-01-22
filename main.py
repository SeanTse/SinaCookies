import SinaCookies
import requests

MainPage = "https://weibo.com/"
target_url = "https://weibo.com/wflanker?is_all=1"
cookies = SinaCookies.get_cookies_as_visitors()
if cookies:
    r = requests.get(target_url, cookies=cookies)
    with open('dump.html', 'wb') as fd:
            fd.write(r.content)