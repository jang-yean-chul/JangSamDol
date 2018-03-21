from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.set_page_load_timeout(30)

driver.get("http://www.naver.com")

driver.maximize_window()

driver.implicitly_wait(20)

driver.get_screenshot_as_file("naver1.png")

driver.find_element_by_id("id").send_keys("")

driver.find_element_by_id("pw").send_keys("")

driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/span/input").click()

time.sleep(10)

driver.get_screenshot_as_file("naver2.png")

driver.find_element_by_xpath("//*[@id='svc.blog']/span").click()

time.sleep(1)

driver.get_screenshot_as_file("naver3.png")

driver.find_element_by_xpath("//*[@id='container']/div[3]/ul[2]/li[1]/a").click()

time.sleep(1)

driver.get_screenshot_as_file("naver4.png")

driver.get("http://blog.naver.com/ajh910/postwrite?categoryNo=29")

time.sleep(5)

driver.get_screenshot_as_file("naver5.png")
driver.find_element_by_xpath("//*[@id='subject']").clear()
driver.find_element_by_xpath("//*[@id='subject']").send_keys("hello")
driver.switch_to.frame("SmartEditorIframe")

driver.find_element_by_css_selector("body").send_keys("dddddddddddddddddddddddddddddddd")
driver.switch_to.default_content()

time.sleep(5)

driver.get_screenshot_as_file("naver6.png")

# driver.find_element_by_tag_name("body.se2_inputarea").send_keys("hello")


time.sleep(5)

driver.get_screenshot_as_file("naver7.png")

driver.quit()