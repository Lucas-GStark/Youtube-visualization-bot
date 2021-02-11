from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep

def main(url):
    
    base = "https://www.youtube.com/"

    session = HTMLSession()

    req = session.get(url)
    req.html.render(sleep=1, timeout=30)

    video_title = []
    video_link = []

    videos_table = req.html.find("#items")
    for video_table in videos_table:
        video = video_table.find("#video-title")
        for title in video:
            video_title.append(title.text)
        for link in video:
            video_link.append(base + link.attrs["href"])
    
    run = True
    while run:
        
        path = "C:\\Users\lucas\OneDrive\Área de Trabalho\Webdriver\edgedriver.exe"

        driver = webdriver.Edge(path)
        for link in video_link:
            driver.get(link)
            sleep(120)

url = "https://www.youtube.com/channel/UC_7e8TJhyU_84USJuHMWJ0g/videos"
main(url)