# base中放最基础的元素操作方法-需要定位元素对象②---定位元素对象需要调用驱动对象①
# -目前涉及到登录模块--有点击方法③、输入框的输入方法④、
# 获取 昵称⑤ 和 获取 toast⑥ 又是两种方法
# 退出登录需要定位退出--拖拽方法⑦
# 断言失败截图⑧
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 元素定位
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入方法
    def base_input(self, loc, value):
        # 定位元素
        el = self.base_find(loc)
        # 清空输入框
        el.clear()
        # 输入内容
        el.send_keys(value)

    # 获取文本信息
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 获取toast信息 频率和loc --loc在这里封装
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contain(@text.'{}')]".format(msg)
        return self.base_find(loc, poll=0.2)

    # 拖拽元素方法
    def base_drag_and_drop(self, start_loc, end_loc):
        start_el = self.base_find(start_loc)
        end_el = self.base_find(end_loc)
        self.driver.drag_and_drop(start_el, end_el)

        # 截图

    @allure.step(title='正在 截图操作')
    def base_get_img(self):
        self.driver.get_screenshot_as_file("./image/fail.png")
        # 将图片写入报告
        self.base_write_allure()

    # 将图片写入 allure报告
    @allure.step(title='正在 写入报告')
    def base_write_allure(self, title="断言失败原因："):
        with open("./image/fail.png", "rb")as f:
            allure.attach(title, f.read(), allure.attach_type.PNG)

    # 根据文本获取元素并 点击
    def base_text_click(self, text):
        loc = By.XPATH, "//*[contains(@text, '{}')]".format(text)
        self.base_find(loc).click()

    # 获取一组元素定位
    def bage_find_elements(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_elements(*loc))
