#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from json import loads, dumps
from appium import webdriver
from subprocess import Popen
import _thread
import time


# def run_appium_service():
#     a = Popen(['appium'])
#     time.sleep(10)
#     return a


def run_first_test():
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "9.0",
        "deviceName": "Pixel3aAPI28",
        "appPackage": "com.example.fitness_app",
        "appActivity": "MainActivity"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(20)

    # appium_logs = driver.get_log('logcat')

    get_started_btn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
    get_started_btn.click()
    # appium_logs = driver.get_log('logcat')
    time.sleep(10)
    driver.close_app()
    driver.quit()

# a = run_appium_service()
a = Popen(['appium'])
time.sleep(10)
run_first_test()
# time.sleep(10)
# a.terminate()
print("second time")
run_first_test()
a.terminate()
a.wait()
