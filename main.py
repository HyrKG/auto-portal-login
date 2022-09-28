import term_login

if __name__ == '__main__':
    term = term_login.request_term();

    if term.is_logged():
        print("你已登录...!")
    else:
        print("即将尝试登录...")
        # TODO login here
