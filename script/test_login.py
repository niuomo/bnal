import pytest
import os
import sys

sys.path.append(os.getcwd())

from page.page_in import PageIn
from tool.get_driver import DriverUtil


def get_data():
    return [('15028545327', "123456", "niuomo", None)]


class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 获取页面对象
        self.login = PageIn().page_in_login()
        # 点击我 ----只需要操作一次 即可
        self.login.page_click_me()

        # 点击 已有账号去登录  --只需要操作一次即可
        self.login.page_click_have_account()

    # 结束
    def teardown_class(self):
        DriverUtil.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("username, pwd, nickename, expect_toast", get_data())
    def test01_login(self, username, pwd, nickename, expect_toast):
        # 调用业务方法
        self.login.page_login_proxy(username, pwd)
        # 登录成功
        if nickename:
            # 断言
            try:
                assert nickename == self.login.page_get_nickname()
            except Exception as e:
                # 先截图 再抛出异常
                self.login.base_get_image()
                raise e

            finally:
                # 退出登录业务方法
                self.login.page_logout()
                # 点击我
                self.login.page_click_me()
                # 点击已有账号去登录
                self.login.page_click_have_account()

        # 登录失败
        else:
            # 断言
            try:
                assert expect_toast in self.login.page_get_toast(expect_toast)
            except Exception as e:
                # 先截图 再抛出异常
                self.login.base_get_image()
                raise e
