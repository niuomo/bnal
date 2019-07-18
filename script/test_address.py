import os
import sys

sys.path.append(os.getcwd())

import pytest

from page.page_in import PageIn
from tool.get_driver import DriverUtil


# def get_data():
#     # name,phone,province,city,area,info,code
#     return [("张三", "13800001111", "广东省", "湛江市", "坡头区", "XXXX大街108号", "100080")]


def get_data02():
    # name,phone,province,city,area,info,code
    return [("李四", "150288545327", "北京市", "丰台区", "XXXX大学", "100081")]


class TestAddress:
    # 初始化
    def setup_class(self):
        # 获取PageLogin 并 调用 登录方法
        self.login = PageIn().page_in_login()
        self.login.page_login_rely_proxy("15028545327", "123456")
        # 获取PageAddress对象
        self.address = PageIn().page_get_PageAddress()

    # 结束
    def teardown_class(self):
        # 关闭driver
        DriverUtil().quit_driver()

    # # 测试方法
    # @pytest.mark.parametrize("name,phone,province,city,area,info,code", get_data())
    # def test01_post_address(self, name, phone, province, city, area, info, code):
    #     # 调用新增地址业务方法
    #     self.address.page_add_address(name, phone, province, city, area, info, code)
    #     try:
    #         expect_person = name + "  " + phone
    #
    #         assert expect_person in self.address.page_get_address_name_list()
    #         # expect_person_address = province + city + area + info
    #         # assert  expect_person_address in self.address.page_get_address_list()
    #     except:
    #         # 截图
    #         self.address.base_get_img()
    #         # 抛出异常
    #         raise
    #
    #     # 修改地址

    @pytest.mark.parametrize("name,phone,province,area,info,code", get_data02())
    def test01_modify_address(self, name, phone, province, area, info, code):
        self.address.page_modify_proxy(name, phone, province, area, info, code)
