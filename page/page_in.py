# 统一入口类  几个入口几个方法
from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.get_driver import DriverUtil


class PageIn(object):
    # pagelogin入口
    driver = DriverUtil.get_driver()

    # 获取login入口对象
    def page_in_login(self):
        return PageLogin(self.driver)

        # 获取PageAddress对象

    def page_get_PageAddress(self):
        return PageAddress(self.driver)
