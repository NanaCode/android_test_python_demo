# _*_ coding: utf-8 _*_
__author__ = 'Nana'
__date__ = '2018/5/31 22:22'

import os


# app类
class App(object):
    def __init__(self):
        self.content = ""
        self.start_time = 0

    # 启动App
    def launch_app(self):
        cmd = "adb shell am start -W -n com.android.browser/.BrowserActivity"
        self.content = os.popen(cmd)

    # 停止App
    def stop_app(self):
        cmd = "adb shell am force-stop com.android.browser"
        os.popen(cmd)

    # 获取启动时间
    def get_launched_time(self):
        for line in self.content.readlines:
            if "ThisTime" in line:
                self.start_time = line.split(":")[1]
                break
            return self.start_time


class Controller(object):
    def run(self):
        pass

    def collect_all_data(self):
        pass

    def save_data_to_csv(self):
        pass
