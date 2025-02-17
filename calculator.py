import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

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

    def click_clear(self):
        """Helper method to click the clear button"""
        btn_clear = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_c_s")
        btn_clear.click()
    
    def test_1_addition(self):
        """Test case for 2 + 3 = 5"""
        self.driver.tap([(500, 500)])
        self.click_clear()
        btn_2 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_2_s")
        btn_plus = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_plus_s")
        btn_3 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_3_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons for 2 + 3 =
        btn_2.click()
        btn_plus.click()
        btn_3.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        # print(" ")
        print(f"The result of 2 + 3 {result}")

        # Assertion
        assert result == "= 5"


    def test_2_subtraction(self):
        """Test case for 5 - 3 = 2"""

        self.click_clear()

        btn_5 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_5_s")
        btn_minus = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_minus_s")
        btn_3 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_3_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons
        btn_5.click()
        btn_minus.click()
        btn_3.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        print(f"The result of 5 - 3 {result}")

        # Assertion
        assert result == "= 2"


    def test_3_multiplication(self):
        """Test case for 2 * 3 = 6"""

        self.click_clear()

        btn_2 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_2_s")
        btn_mul = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_mul_s")
        btn_3 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_3_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons
        btn_2.click()
        btn_mul.click()
        btn_3.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        print(f"The result of 2 * 3 {result}")

        # Assertion
        assert result == "= 6"


    def test_4_div(self):
        """Test case for 6 / 2 = 3"""

        self.click_clear()

        btn_6 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_6_s")
        btn_div = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_div_s")
        btn_2 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_2_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons
        btn_6.click()
        btn_div.click()
        btn_2.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        print(f"The result of 6 / 2 {result}")

        # Assertion
        assert result == "= 3"

    def test_5_Div_By_Zero(self):
        """Test case for 5 / 0 """

        self.click_clear()

        btn_5 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_5_s")
        btn_div = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_div_s")
        btn_0 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_0_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons
        btn_5.click()
        btn_div.click()
        btn_0.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        print(f"The result of 5 / 0 {result}")

        # Assertion
        assert result == "= Can't divide by zero"


    def test_6_Decimals(self):
        """Test case for 5.1 + 2.1 = 7.2 """

        self.click_clear()

        btn_5 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_5_s")
        btn_dot = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_dot_s")
        btn_1 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_1_s")
        btn_add = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_plus_s")
        btn_2 = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_2_s")
        btn_equals = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/btn_equal_s")

        # Click the buttons
        btn_5.click()
        btn_dot.click()
        btn_1.click()
        btn_add.click()
        btn_2.click()
        btn_dot.click()
        btn_1.click()
        btn_equals.click()

        # Try to get the result
        result = self.driver.find_element(by=AppiumBy.ID, value="com.miui.calculator:id/result").text.strip()
        print(f"The result of 5.1 + 2.1 {result}")

        # Assertion
        assert result == "= 7.2"