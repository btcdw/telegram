# -*- coding:UTF-8 -*-
import zipfile
import shutil
import win32process
import time
import os
import tkinter.messagebox


from tkinter import *
import tkinter as tk  # 使用Tkinter前需要先导入

程序PID = list_pid2 = []

list = [r"0\Telegram.exe", r"1\Telegram.exe", r"2\Telegram.exe", r"3\Telegram.exe", r"4\Telegram.exe",
        r"5\Telegram.exe", r"6\Telegram.exe", r"7\Telegram.exe", r"8\Telegram.exe", r"9\Telegram.exe",
        r"10\Telegram.exe"]


def 解压电报文件方法():
    zip_file = zipfile.ZipFile("0.zip")
    zip_list = zip_file.namelist()  # 得到压缩包里所有文件
    for f in zip_list:
        zip_file.extract(f, )  # 循环解压文件到指定目录
    zip_file.close()  # 关闭文件，必须有，释放内存
    # 把文件夹复制10遍
    for i in range(1, 11):
        source_path = os.path.abspath(r'0')
        target_path = os.path.abspath(str(i))
        if not os.path.exists(target_path):
            # 如果目标路径不存在原文件夹的话就创建
            os.makedirs(target_path)
        if os.path.exists(source_path):
            # 如果目标路径存在原文件夹的话就先删除
            shutil.rmtree(target_path)
        shutil.copytree(source_path, target_path)
    print('10个应用程序复制完成')


def 应用程序方法():
    for i in range(1, s2.get()+ 1):
        handle = win32process.CreateProcess(list[i], '', None, None, 0, win32process.CREATE_NO_WINDOW,
                                        None, None, win32process.STARTUPINFO())
        xx = str(handle[2])
        list_pid2.append(xx)
        time.sleep(600)  # 10分钟后关闭应用程序
        关闭所有程序()
        tk.messagebox.showinfo("到期提醒","10分钟试用结束！")


def 关闭所有程序():
    for i in 程序PID:
        # print(i)
        # print(r'taskkill /F /IM {}'.format(i))
        os.system(r'taskkill /F /IM {}'.format(i))

if __name__ == "__main__":

    程序 = os.path.exists('10')
    if 程序 == False:
        解压电报文件方法()
        print("初始化完成，请重启应用程序")
    else:
        # print("非第一次运行")

        # 第1步，实例化object，建立窗口window
        window = tk.Tk()

        # 第2步，给窗口的可视化起名字
        window.title('电报妹Telegram多开助手V2.8.11')

        # 第3步，设定窗口的大小(长 * 宽)
        window.geometry('350x150')  # 这里的乘是小x

        # 第4步，在图形界面上设定标签
        l = tk.Label(window, text='滑动下方数量选择启动数量', bg='green', font=('Arial', 12), width=30, height=2)
        # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

        # 第5步，放置标签
        l.pack()  # Label内容content区域放置位置，自动调节尺寸
        # 放置lable的方法有：1）l.pack(); 2)l.place();

        s2 = Scale(window, from_=0, to=10, orient=HORIZONTAL)
        s2.pack()

        Button(window, text="点击运行", command=应用程序方法).pack()

        mainloop()
        # 第6步，主窗口循环显示
        window.mainloop()
        # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环

