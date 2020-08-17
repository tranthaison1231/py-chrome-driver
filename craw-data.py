from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path="./chromedriver")

browser.get("https://school.coders-x.com/login")


user = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div/form/div[1]/div/input")


user.send_keys("thaison.coderstokyo@gmail.com")

password = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div/form/div[2]/div/input")

password.send_keys("gesuvuma")


loginBtn = browser.find_element_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div/form/div[3]/div[1]/button")

loginBtn.click()

sleep(5)


browser.close()
