from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import smtplib


url = input()

def check_price():
    ser = Service("C:\\Users\\josep\\Downloads\\chromedriver_win32\\chromedriver.exe")
    op = webdriver.ChromeOptions()
    op.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ser, options=op)

    driver.get(url)
    driver.maximize_window()

    likes = driver.find_element(By.XPATH, "//span[contains(@class,'Text SmallTitle ListingPage-Likes-Count')]").text

    product = driver.find_element(By.XPATH, "//p[contains(@class,'Text Body ListingPage-Details-Detail')]").text

    first_count = 15
    second_count = 30

    if int(likes) == first_count:
        send_mail(first_count)
    if int(likes) == second_count:
        send_mail(second_count)

def send_mail(count):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('grailedalerts@gmail.com', )
