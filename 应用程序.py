# -*- coding: gbk -*-
import zipfile
import shutil
import win32process
import time
import os
import tkinter.messagebox


from tkinter import *
import tkinter as tk  # ʹ��Tkinterǰ��Ҫ�ȵ���

����PID = list_pid2 = []

list = [r"0\Telegram.exe", r"1\Telegram.exe", r"2\Telegram.exe", r"3\Telegram.exe", r"4\Telegram.exe",
        r"5\Telegram.exe", r"6\Telegram.exe", r"7\Telegram.exe", r"8\Telegram.exe", r"9\Telegram.exe",
        r"10\Telegram.exe"]


def ��ѹ�籨�ļ�����():
    zip_file = zipfile.ZipFile("0.zip")
    zip_list = zip_file.namelist()  # �õ�ѹ�����������ļ�
    for f in zip_list:
        zip_file.extract(f, )  # ѭ����ѹ�ļ���ָ��Ŀ¼
    zip_file.close()  # �ر��ļ��������У��ͷ��ڴ�
    # ���ļ��и���10��
    for i in range(1, 11):
        source_path = os.path.abspath(r'0')
        target_path = os.path.abspath(str(i))
        if not os.path.exists(target_path):
            # ���Ŀ��·��������ԭ�ļ��еĻ��ʹ���
            os.makedirs(target_path)
        if os.path.exists(source_path):
            # ���Ŀ��·������ԭ�ļ��еĻ�����ɾ��
            shutil.rmtree(target_path)
        shutil.copytree(source_path, target_path)
    print('10��Ӧ�ó��������')


def Ӧ�ó��򷽷�():
    for i in range(1, s2.get()+ 1):
        handle = win32process.CreateProcess(list[i], '', None, None, 0, win32process.CREATE_NO_WINDOW,
                                        None, None, win32process.STARTUPINFO())
        xx = str(handle[2])
        list_pid2.append(xx)
        time.sleep(600)  # 10���Ӻ�ر�Ӧ�ó���
        �ر����г���()
        tk.messagebox.showinfo("��������","10�������ý�����")


def �ر����г���():
    for i in ����PID:
        # print(i)
        # print(r'taskkill /F /IM {}'.format(i))
        os.system(r'taskkill /F /IM {}'.format(i))

if __name__ == "__main__":

    ���� = os.path.exists('10')
    if ���� == False:
        ��ѹ�籨�ļ�����()
        print("��ʼ����ɣ�������Ӧ�ó���")
    else:
        # print("�ǵ�һ������")

        # ��1����ʵ����object����������window
        window = tk.Tk()

        # ��2���������ڵĿ��ӻ�������
        window.title('�籨��Telegram�࿪����V2.8.11')

        # ��3�����趨���ڵĴ�С(�� * ��)
        window.geometry('350x150')  # ����ĳ���Сx

        # ��4������ͼ�ν������趨��ǩ
        l = tk.Label(window, text='�����·�����ѡ����������', bg='green', font=('Arial', 12), width=30, height=2)
        # ˵���� bgΪ������fontΪ���壬widthΪ����heightΪ�ߣ�����ĳ��͸����ַ��ĳ��͸ߣ�����height=2,���Ǳ�ǩ��2���ַ���ô��

        # ��5�������ñ�ǩ
        l.pack()  # Label����content�������λ�ã��Զ����ڳߴ�
        # ����lable�ķ����У�1��l.pack(); 2)l.place();

        s2 = Scale(window, from_=0, to=10, orient=HORIZONTAL)
        s2.pack()

        Button(window, text="�������", command=Ӧ�ó��򷽷�).pack()

        mainloop()
        # ��6����������ѭ����ʾ
        window.mainloop()
        # ע�⣬loop��Ϊ��ѭ������˼��window.mainloop�ͻ���window���ϵ�ˢ�£����û��mainloop,����һ����̬��window,�����ȥ��ֵ�Ͳ�����ѭ����mainloop���൱��һ���ܴ��whileѭ�����и�while��ÿ���һ�ξͻ����һ�Σ��������Ǳ���Ҫ��ѭ��

