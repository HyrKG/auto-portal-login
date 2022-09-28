import os

import term_login
import configparser
from time import sleep

config = configparser.ConfigParser()

account = None
term_type = None
config_path = None
passwd = None


def spawn_and_read_config():
    global config_path
    config_path = os.path.join(os.getcwd(), "auto-pl-config.ini")
    config.read(config_path)

    if not os.path.exists(config_path):
        config.add_section("general")
        config.set("general", "term-type", str(1))
        config.set("general", "account", "your-account-here")
        config.set("general", "password", "your-passwd-here")
        config.write(open(config_path, 'a'))
        print(fr"已生成配置于 {config_path} ,请完成配置后再次开启！该界面将于10秒后关闭！")
        sleep(10)
        exit()
    else:
        global term_type
        term_type = int(config.get("general", "term-type"))
        global account
        account = config.get("general", "account")
        global passwd
        passwd = config.get("general", "password")


if __name__ == '__main__':
    # 保存或读取配置
    spawn_and_read_config()

    # 至多允许尝试60次
    retryTimes: int = 1
    closeFlag: bool = False

    while not closeFlag and retryTimes <= 120:
        # 发起请求，补全term
        print("正在联系169.cn中...x" + str(retryTimes))

        term = None
        try:
            term = term_login.request_term();
        except Exception:
            print('发生了错误!请等待重试...')

        if term is not None:
            if term.is_logged():
                print("你已登录...!")
                closeFlag = True
            else:
                print("即将尝试登录...")
                if account is None or account == "your-account-here":
                    print(fr"已生成配置于 {config_path} ,请完成配置后再次开启！该界面将于10秒后关闭！")
                    sleep(10)
                    exit()
                else:
                    term.termtype = term_type
                    result = term.login(account, passwd)
                    print(result)
        if not closeFlag:
            print("....等待下一次验证")
        retryTimes += 1
        sleep(1)

    if not closeFlag:
        print("无法连接，请确保电脑会自动连接校园网！")
    print("")
    print("#> 程序结束，将在3秒后退出")
    sleep(3)
    print("...exit")
