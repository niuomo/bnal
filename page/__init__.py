from selenium.webdriver.common.by import By

"""pagelogin页面的元素地位"""

# 我的按钮
login_me_but = By.XPATH, "//*[@text='我']"
# 已有账号 去登录
login_have_account = By.ID, "com.yunmall.lc:id/textView1"
# 用户名 ---最好别用文字 ---输入一次之后文字就改变了--不能再次定位 无法进行后续操作
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_login_but = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

'''个人设置页面'''
# 短信提醒
setting_msg = By.ID, 'com.yunmall.lc:id/setting_sms_notify'
# 修改密码
setting_change_pwd = By.ID, 'com.yunmall.lc:id/setting_modify_pwd'
# 退出按钮
setting_quit_but = By.ID, 'com.yunmall.lc:id/setting_logout'
# 退出确认按钮
setting_quit_ok_but = By.ID, 'com.yunmall.lc:id/ymdialog_right_button'
# 地址管理
setting_address = By.ID, 'com.yunmall.lc:id/setting_address_manage'

"""以下数据为地址管理配置数据"""
# 新增地址
address_new = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 电话
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 点击 所在地区
address_province = By.ID, "com.yunmall.lc:id/address_province"
# 选择 省/直辖市 com.yunmall.lc:id/area_title
# 选择 市
# 选择 区
# 详细地址
address_detail_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_postcode = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 收件人  姓名+“  ”+电话
address_name = By.ID, "com.yunmall.lc:id/receipt_name"
# 收件地址
address_add = By.ID, 'com.yunmall.lc:id/receipt_address'
# 地址页面 编辑
address_edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改按钮
address_modify = By.ID, 'com.yunmall.lc:id/modify'

"修改页面"
# 收件人
modify_name = By.ID, 'com.yunmall.lc:id/address_receipt_name'
# 手机号
modify_phone = By.ID, 'com.yunmall.lc:id/address_add_phone'
# 收件人地址
modify_address = By.ID, 'com.yunmall.lc:id/address_province'
# 北京市的北京市
modify_bj = By.ID, 'com.yunmall.lc:id/area_title'
# 收件人详细地址
modify_info = By.ID, 'com.yunmall.lc:id/address_detail_addr_info'
# 收件人邮编
modift_code = By.ID, 'com.yunmall.lc:id/address_post_code'
# 保存按钮
modify_save = By.ID,'com.yunmall.lc:id/button_send'
