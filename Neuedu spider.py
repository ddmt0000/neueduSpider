# Author：ddmt
# url: ddmt.top
# time: 2024-3-5
import time
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

#注意：该爬虫仅用于学习交流，禁止用于任何商业用途。
#     请遵守相关法律法规，该爬虫不会保留任何爬取的文件结果，
#     也不会以任何方式出于非法目的抓取页面内容，请确保在得到授权的情况下使用，
#     使用该爬虫，你仍需要取得账号且获得页面访问权，
#     爬虫的目的仅用于标记和分类管理学习，不当使用可能导致账号出现问题。
#     你需要承认全部因此带来的后果和责任，故请确保你已有完全刑事能力。

host = "https://gzyy.neuedu.com" #域名
username = "" #用户名
password = "" #密码

driver.get(f"{host}/learn/280/?type=2") #跳转到登陆页面
wait = WebDriverWait(driver, 10) 
element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/form/div[1]/div/div/input').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/form/div[2]/div/div/input').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/form/div[3]/div/button').click()
xpath_span_expression = '//*[@id="app"]/div/div[2]/div/div[1]/span[4]/span[1]'
r = open("video_list_175_280.txt", "a", encoding="utf-8")

for i in range(280,338): #爬取页面范围
    time.sleep(1) # 等待页面加载 （必要的）
    driver.get(f"{host}/learn/{i}/?type=2")
    time.sleep(3)
    span_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath_span_expression))
    )
    span_title = span_element.text
    page_content = driver.page_source
    doc = html.fromstring(page_content)
    video_sources = doc.xpath("//video/@src")
    first_video_src = video_sources[0] if video_sources else None
    if first_video_src:
        print(f"First video source URL: {first_video_src}")
        r.write(f"[title:{span_title}]: {host}{first_video_src}\n") # 写入文件格式化（实例：[title:xxxx]: https://gzyy.neuedu.com/xxxx）
    time.sleep(1)

#以上sleep均是为了保证程序运行稳定，非必要且时间可调

#关闭
r.close()
driver.quit()