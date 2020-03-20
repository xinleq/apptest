import time

from base.initDriver import init_driver
class TestToast:
    def setup(self):
        self.driver=init_driver()
    def test_get_toast(self):
        time.sleep(5)

        self.driver.press_keycode(4)
        # self.driver.keyevent(4)py
        self.driver.find_element_by_id("com.android.haitong:id/dlg_tv_ok").click()