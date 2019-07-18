import page
from base.base import Base


class PageAddress(Base):
    # 点击 新增地址
    def page_click_add_address(self):
        self.base_click(page.address_new)

    # 输入 收件人
    def page_input_receiver(self, name):
        self.base_input(page.address_receipt_name, name)

    # 输入 手机号
    def page_input_phone(self, phone):
        self.base_input(page.address_add_phone, phone)

    # 点击 所在地区
    def page_click_area(self):
        self.base_click(page.address_province)

    # 选择 省/直辖市
    def page_click_province(self, province):
        self.base_text_click(province)

    # 选择 市
    def page_click_city(self, city):
        self.base_text_click(city)

    # 选择 区
    def page_click_small_area(self, area):
        self.base_text_click(area)

    # 输入 详细地址
    def page_click_address_info(self, address):
        self.base_input(page.address_detail_info, address)

    # 输入 邮编
    def page_input_code(self, code):
        self.base_input(page.address_postcode, code)

    # 设为默认地址
    def page_default_address(self):
        self.base_click(page.address_default)

    # 保存
    def page_click_save(self):
        self.base_click(page.address_save)

    # 组合输入地址-业务方法
    def page_add_address(self, name, phone, province, city, area, info, code):
        self.page_click_add_address()
        self.page_input_receiver(name)
        self.page_input_phone(phone)
        self.page_click_area()
        self.page_click_province(province)
        self.page_click_city(city)
        self.page_click_small_area(area)
        self.page_click_address_info(info)
        self.page_input_code(code)
        self.page_default_address()
        self.page_click_save()

    # 获取地址列表一组元素
    def page_get_address_name_list(self):
        el = self.bage_find_elements(page.address_name)
        # print(el)
        return [i.text for i in el]

    def page_get_address_list(self):
        el = self.bage_find_elements(page.address_add)
        # print(el)
        return [i.text for i in el]

    # 点击编辑按钮
    def page_click_edit_but(self):
        self.base_click(page.address_edit)

    # 获取修改列表文本信息
    def page_click0_modify_list(self):
        self.bage_find_elements(page.address_modify)[1].click()
        # return [i.text for i in el]

    # 修改-输入收件人
    def page_modify_name(self, name):
        self.base_input(page.modify_name, name)

    # 修改-输入电话
    def page_modify_phone(self, phone):
        self.base_input(page.modify_phone, phone)

    # 点击收件人的地址
    def page_modify_click_where(self):
        self.base_click(page.modify_address)

    # 直接点击北京
    def page_click_bj(self):
        print(self.base_find(page.modify_bj).text)
        self.base_click(page.modify_bj)

    # 输入详细地址
    def page_modity_input_info(self, info):
        self.base_input(page.modify_info, info)

    # 输入邮编
    def page_modify_code(self, code):
        self.base_input(page.modift_code, code)

    # 点击保存
    def page_modify_save_info(self):
        self.base_click(page.modify_save)

    # 组合修改业务
    def page_modify_proxy(self, name, phone, province, area, info, code):
        self.page_click_edit_but()
        self.page_click0_modify_list()
        self.page_modify_name(name)
        self.page_modify_phone(phone)
        self.page_modify_click_where()
        self.page_click_province(province)
        self.page_click_bj()
        self.page_click_small_area(area)
        self.page_modity_input_info(info)
        self.page_modify_code(code)
        self.page_modify_save_info()
