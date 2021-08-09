import time
def open_age(driver,url):
    driver.maximize_window()
    driver.get(url)

def login(driver,username,password):
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
    driver.find_element_by_xpath("//button[@id='btnSubmit']").click()

def seach(driver,key,url,username,password):
    open_age(driver, url)
    login(driver, username, password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    id_iframe = id + '-frame'
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys(key)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(2)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num