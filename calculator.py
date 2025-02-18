import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

# Constants for button IDs
BTN_MORE_OPERATIONS = "com.miui.calculator:id/btn_switch"
BTN_MORE = "com.miui.calculator:id/ic_cal_more"
BTN_HISTORY = "com.miui.calculator:id/ll_setting_history"
BTN_PARANTHESIS_LEFT = "com.miui.calculator:id/btn_lp"
BTN_PARANTHESIS_RIGHT = "com.miui.calculator:id/btn_rp"
BTN_CLEAR = "com.miui.calculator:id/btn_c_s"
BTN_1 = "com.miui.calculator:id/btn_1_s"
BTN_2 = "com.miui.calculator:id/btn_2_s"
BTN_3 = "com.miui.calculator:id/btn_3_s"
BTN_5 = "com.miui.calculator:id/btn_5_s"
BTN_6 = "com.miui.calculator:id/btn_6_s"
BTN_0 = "com.miui.calculator:id/btn_0_s"
BTN_PLUS = "com.miui.calculator:id/btn_plus_s"
BTN_MINUS = "com.miui.calculator:id/btn_minus_s"
BTN_MUL = "com.miui.calculator:id/btn_mul_s"
BTN_DIV = "com.miui.calculator:id/btn_div_s"
BTN_EQUALS = "com.miui.calculator:id/btn_equal_s"
BTN_DOT = "com.miui.calculator:id/btn_dot_s"
RESULT = "com.miui.calculator:id/result"

@pytest.fixture(scope="class", autouse=True)
def driver(request):
    # Create an instance of Appium options
    options = AppiumOptions()

    # Set capabilities
    options.set_capability("platformName", "Android")
    options.set_capability("deviceName", "651d22fe0510")
    options.set_capability("udid", "651d22fe0510")
    options.set_capability("appPackage", "com.miui.calculator")
    options.set_capability("appActivity", "com.miui.calculator.cal.CalculatorActivity")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("platformVersion", "13")

    # Start the driver
    driver = webdriver.Remote("http://localhost:4723", options=options)

    # Adding the driver instance to the test class
    request.cls.driver = driver

    yield driver  # This will keep the driver open for all tests in the class

    driver.quit()  # Quit the driver after all tests in the class are done

@pytest.mark.usefixtures("driver")
class TestCalculator:

    def click_button(self, button_id):
        """Helper method to click a button by its ID"""
        button = self.driver.find_element(by=AppiumBy.ID, value=button_id)
        button.click()

    def get_result(self):
        """Helper method to retrieve the result from the calculator"""
        result_element = self.driver.find_element(by=AppiumBy.ID, value=RESULT)
        return result_element.text.strip()

    def click_clear(self):
        """Click the clear button to reset the calculator"""
        self.click_button(BTN_CLEAR)

    def test_1_addition(self):
        """Test case for 2 + 3 = 5"""
        self.driver.tap([(500, 500)])

        self.click_clear()
        self.click_button(BTN_2)
        self.click_button(BTN_PLUS)
        self.click_button(BTN_3)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 2 + 3 {result}")
        assert result == "= 5"

    def test_2_subtraction(self):
        """Test case for 5 - 3 = 2"""
        self.click_clear()
        self.click_button(BTN_5)
        self.click_button(BTN_MINUS)
        self.click_button(BTN_3)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 5 - 3 {result}")
        assert result == "= 2"

    def test_3_multiplication(self):
        """Test case for 2 * 3 = 6"""
        self.click_clear()
        self.click_button(BTN_2)
        self.click_button(BTN_MUL)
        self.click_button(BTN_3)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 2 * 3 {result}")
        assert result == "= 6"

    def test_4_div(self):
        """Test case for 6 / 2 = 3"""
        self.click_clear()
        self.click_button(BTN_6)
        self.click_button(BTN_DIV)
        self.click_button(BTN_2)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 6 / 2 {result}")
        assert result == "= 3"

    def test_5_Div_By_Zero(self):
        """Test case for 5 / 0"""
        self.click_clear()
        self.click_button(BTN_5)
        self.click_button(BTN_DIV)
        self.click_button(BTN_0)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 5 / 0 {result}")
        assert result == "= Can't divide by zero"

    def test_6_Decimals(self):
        """Test case for 5.1 + 2.1 = 7.2"""
        self.click_clear()
        self.click_button(BTN_5)
        self.click_button(BTN_DOT)
        self.click_button(BTN_1)
        self.click_button(BTN_PLUS)
        self.click_button(BTN_2)
        self.click_button(BTN_DOT)
        self.click_button(BTN_1)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 5.1 + 2.1 {result}")
        assert result == "= 7.2"

    def test_8_History(self):
        """Test case for paranthesis"""
        self.click_clear()
        self.click_button(BTN_MORE_OPERATIONS)
        self.click_button(BTN_1)
        self.click_button(BTN_MINUS)
        self.click_button(BTN_PARANTHESIS_LEFT)
        self.click_button(BTN_3)
        self.click_button(BTN_MINUS)
        self.click_button(BTN_2)
        self.click_button(BTN_PARANTHESIS_RIGHT)
        self.click_button(BTN_EQUALS)

        result = self.get_result()
        print(f"The result of 1 - (3 - 2) {result}")
        assert result == "= 0"

        self.click_button(BTN_MORE)
        self.click_button(BTN_HISTORY)

        time.sleep(10)
        