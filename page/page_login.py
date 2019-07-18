# 页面层（继承基类）--你做的具体操作流程-包括最终目的的成功与失败--登录--》登录成功、登录失败
# 最后的最后 组合业务
import page
from base.base import Base


class PageLogin(Base):
    # 具体的操作步骤:
    # 点击  我
    def page_click_me(self):
        self.base_click(page.login_me_but)

    # 点击  已有账户，去登录
    def page_click_have_account(self):
        self.base_click(page.login_have_account)

    # 输入  用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入  密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击  登录按钮 ---分两种结果--成功还是失败
    def page_click_login(self):
        self.base_click(page.login_login_but)

    # 登录成功 -获取成功后的昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 登录失败 -获取toast提示消息
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 点击设置按钮
    def page_click_setting_but(self):
        self.base_click(page.login_setting)

    # 拖拽，将短信提醒拖拽到修改密码
    def page_drog_and_drop_to_modify_pwd(self):
        self.base_drag_and_drop(page.setting_msg, page.setting_change_pwd)

    # 点击退出按钮
    def page_click_quit_button(self):
        self.base_click(page.setting_quit_but)

    # 点击确认退出按钮
    def page_click_quit_ok_but(self):
        self.base_click(page.setting_quit_ok_but)

    # 点击地址管理
    def page_address_manager(self):
        self.base_click(page.setting_address)

    # 点击退出登录业务方法---这里吧设置放进来了--因为只使用了一次
    def page_logout(self):
        self.page_click_setting_but()
        self.page_drog_and_drop_to_modify_pwd()
        self.page_click_quit_button()
        self.page_click_quit_ok_but()

    # 最后的最后组合业务---只组合同一个界面的业务
    def page_login_proxy(self, username, pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()

    # 新增收件地址的依赖问题
    def page_login_rely_proxy(self,username,pwd):
        self.page_click_me()
        self.page_click_have_account()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login()
        self.page_click_setting_but()
        self.page_address_manager()
