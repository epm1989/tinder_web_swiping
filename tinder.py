from selenium import  webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import  sleep
driver=webdriver.Firefox(executable_path='./drivers/geckodriver')
driver.get("https://tinder.com/")
driver.implicitly_wait(10)

while True:
    """wait for manual login"""
    sleep(5)
    if driver.current_url == "https://tinder.com/app/recs":
        break
c = 0
while c < 5000:
    try:
        source = driver.page_source
        print("source_page")
        no_thanks = "/html/body/div[2]/div/div/button[2]"
        button_no_thanks = driver.find_elements_by_xpath(no_thanks)
        if button_no_thanks and "No Thanks" in source and "Send Super Like" in source:
            print("inside IF")
            button_no_thanks = driver.find_element_by_xpath(no_thanks)
            button_no_thanks.click()

        like = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button"
        button_like = driver.find_element_by_xpath(like)
        button_like.click()
        c += 1
        sleep(3)
    except ElementClickInterceptedException as err:
        print(repr(err)[:50])
        driver.refresh()
        driver.implicitly_wait(3)
        sleep(5)
    except NoSuchElementException as err:
        print(repr(err)[:50])
        sleep(5)
        driver.refresh()
        driver.implicitly_wait(20)


