# 获取和退出两个方法 要用类
from appium import webdriver


class DriverUtil(object):
    # 单例
    driver = None

    # 获取 驱动对象
    @classmethod
    def get_driver(cls):
        # 如果 驱动对象为空--如果驱动对象不存在
        if not cls.driver:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.56.101:5555'
            desired_caps['appPackage'] = 'com.yunmall.lc'
            desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
            # 中文
            desired_caps['unicodeKeyboard'] = True
            desired_caps['resetKeyboard'] = True
            # 获取toast消息
            desired_caps['automationName'] = 'Uiautomator2'
            # 不重置应用
            desired_caps['noRest'] = True
            # 获取driver
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 无论driver存不存在 都要返回driver 所以在driver外
        return cls.driver

    # 退出驱动对象
    @classmethod
    def quit_driver(cls):
        # 如果驱动对象存在
        if cls.driver:
            cls.driver.quit()
            # 释放内存
            cls.driver = None
