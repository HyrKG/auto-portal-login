from urllib.parse import urlparse, parse_qs

import requests

# 请求的地址
REQUEST_LOGIN_URL: str = "http://{0}:801/eportal/?c=Portal&a=login"
REQUEST_LOGOUT_URL: str = "http://{0}:801/eportal/?c=Portal&a=logout"
REQUEST_QUERY = "login_method={0}&" \
                "user_account={1}&" \
                "user_password={2}&" \
                "wlan_user_ip={3}&" \
                "wlan_user_ipv6=&" \
                "wlan_user_mac=000000000000&" \
                "wlan_ac_ip={4}&" \
                "wlan_ac_name={5}&" \
                "jsVersion=3.1"


class Term:
    netloc: str = ''
    # 访问设备:0-PC；1-手机
    termtype: int = 1
    login_method: int = 1
    wlanacname: str = None
    wlanacip: str = None
    wlanuserip: str = None
    usermac: str = None
    url: str = None

    def parser_url_query(self, url: str):
        result = urlparse(url)
        self.netloc = result.netloc
        params: dict = parse_qs(result.query, keep_blank_values=True)
        self.wlanacname = read_dict(params, 'wlanacname')
        self.wlanacip = read_dict(params, 'wlanacip')
        self.wlanuserip = read_dict(params, 'wlanuserip')
        self.usermac = read_dict(params, 'usermac')
        self.url = read_dict(params, 'url')

    def login(self, account: str, password: str):
        url = format_pattern(REQUEST_LOGIN_URL, [self.netloc])
        query = format_pattern(REQUEST_QUERY,
                               [self.login_method, str(f'%2C{self.termtype}%2C') + account, password, self.wlanuserip,
                                self.wlanacip,
                                self.wlanacname])
        complete_url = url + "&" + query
        return requests.get(complete_url).content

    def is_valid(self, except_netloc: str) -> bool:
        return len(self.netloc.strip()) > 0 and self.netloc == except_netloc

    def is_logged(self) -> bool:
        return self.is_valid("www.189.cn")


def read_dict(d: dict, key: str) -> str:
    if key in d:
        return d.get(key)[0]
    return ''


def format_pattern(source: str, args):
    index = 0
    for arg in args:
        source = source.replace("{" + str(index) + "}", str(arg))
        index += 1
    return source


def url2term(url: str) -> Term:
    newTerm: Term = Term()
    newTerm.parser_url_query(url)
    return newTerm


def request_term() -> Term:
    """
    向中国电信请求url，并且加载为term
    :return:
    """
    response = requests.get("http://www.189.cn/?isReback=1")
    return url2term(response.url)
