#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import os
import platform

token = ""
def getanswer(text, token):
    if (token == False):
        return False
    headers = {
        "Host": "app.51xuexiaoyi.com",
        "token": token,
        "device": "Auhqehd3s6Ml6mXky_5dV-Uv4zsdXeUYY7wKFktkH1ag",
        "platform": "android",
        "app-version": "1.1.2",
        "t": "1592904062239",
        "s": "e6a47dea8298225b1e9a9366bead8083",
        "content-type": "application/json;charset=utf-8",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/3.11.0"
    }
    url = "https://app.51xuexiaoyi.com/api/v1/searchQuestion?keyword=" + text
    res = requests.post(url, headers=headers)
    r = res.json()
    if (r['code'] == 200):
        return r['data']
    else:
        return r['msg']


def outanswer(li):
    if isinstance(li, list):
        for i in li:
            print('问题:')
            print(i['q'])
            print('答案:')
            print(i['a'])
            print('-' * 50)
    else:
        print(li)


def login():
    username = input("请输入账号:")
    password = input("请输入密码:")
    url = "https://app.51xuexiaoyi.com/api/v1/login?username=" + username + "&password=" + password
    headers = {
        "Host": "app.51xuexiaoyi.com",
        "device": "Auhqehd3s6Ml6mXky_5dV-Uv4zsdXeUYY7wKFktkH1ag",
        "platform": "android",
        "app-version": "1.1.2",
        "t": "1593008524987",
        "s": "53029a76022a2f4a52c11f08a84759c0",
        "Content-Type": "application/json; charset=utf-8",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.11.0"
    }
    res = requests.post(url, headers=headers).json()
    if (res['code'] == 200):
        f = open('token.txt', 'w+')
        f.write(res['data']['api_token'])
        f.close()
        print("登陆成功!")
        return res['data']['api_token']
    else:
        return res['msg']


def main():
    print('输入"exit"或点"x"即可退出')
    print('直接输入题目即可获取答案')
    try:
        f = open('token.txt', 'r+')
        token = f.read()
        f.close()
        if (token == ""):
            print('第一次使用请登录学小易账号')
            token = login()
            print("这里是空")
    except:
        token = login()
    while True:
        questions = input(">>>")
        sys = platform.system()
        if sys == "Windows":
            os.system('cls')
        elif sys == "Linux":
            os.system('clear')
        if len(questions) >= 6:
            res = getanswer(questions, token)
            outanswer(res)
        elif questions == 'exit':
            break
        else:
            print("题目必须大于6个字符")
    exit()


if __name__ == "__main__":

    main()
