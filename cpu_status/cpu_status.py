# _*_ coding: utf-8 _*_
import csv

__author__ = 'Nana'
__date__ = '2018/6/4 7:01'

import os
import time


# 控制类
class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.all_data = [("timestamp", "cpustatus")]

    # 单次测试过程
    def test_process(self):
        result = os.popen("adb shell dumpsys cpuinfo | grep com.android.browser")
        for line in result.readlines():
            cpu_value = line.split("%")[0]
        current_time = self.get_current_time()
        self.all_data.append(current_time, cpu_value)

    # 多次执行过程
    def run(self):
        while self.counter > 0:
            self.test_process()
            self.counter = self.counter - 1
            time.sleep(5)

    # 获取当前时间戳
    def get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    def save_data_to_csv(self):
        csv_file = file("cpustatus.csv", "wb")
        writer = csv.writer(csv_file)
        writer.writerows(self.all_data)
        csv_file.close()

if __name__ == '__main__':
    controller = Controller(10)
    controller.run()
    controller.save_data_to_csv()