import os

import term_login
import configparser

config = configparser.ConfigParser()

account = None
term_type = None
config_path = None
passwd = None


def spawn_and_read_config():
    global config_path
    config_path = os.path.join(os.getcwd(), "config.ini")
    config.read(config_path)

    if not os.path.exists(config_path):
        config.add_section("general")
        config.set("general", "term-type", str(1))
        config.set("general", "account", "your-account-here")
        config.set("general", "password", "your-passwd-here")
        config.write(open(config_path, 'a'))
        print(fr"已生成配置于 {config} ,请完成配置后再次开启！")
    else:
        global term_type
        term_type = int(config.get("general", "term-type"))
        global account
        account = config.get("general", "account")
        global passwd
        passwd = config.get("general", "password")


if __name__ == '__main__':

    term = term_login.request_term();
    spawn_and_read_config()

    print("正在联系169.cn中...")
    if term.is_logged():
        print("你已登录...!")
    else:
        print("即将尝试登录...")
        if account == None or account == "your-account-here":
            print(fr"请先完成配置! {config_path}")
        else:
            term.termtype = term_type
            term.login(account, passwd)
            print("执行完成，若回执中result为1则表示登录成功...!")
