# _*_ coding: utf-8 _*_
import csv
import time

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


# 控制类
class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.all_data = [("timestamp", "elapsedtime")]

    # 单次测试过程
    def test_process(self):
        self.app.launch_app()
        time.sleep(5)
        elapsed_time = self.app.get_launched_time()
        self.app.stop_app()
        time.sleep(3)
        current_time = self.get_current_time()
        self.all_data.append(current_time, elapsed_time)

    # 多次执行测试过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    # def collect_all_data(self):
    #     pass

    # 数据的存储
    def save_data_to_csv(self):
        csv_file = file("starttime.csv", "wb")
        writer = csv.writer(csv_file)
        writer.writerows(self.all_data)
        csv_file.close()


if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.save_data_to_csv()
