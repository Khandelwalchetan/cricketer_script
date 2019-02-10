#to input the cricketer's name
#importing libraries and modules
from selenium import webdriver
import requests
import bs4 



cricketer_name=input('Enter the name of any cricketer ')

chromedriver=r"C:\Users\Chetan\Downloads\chromedriver_win32\chromedriver.exe"
browser=webdriver.Chrome(chromedriver)

browser.get('https://m.cricbuzz.com/cricket-search/player/tit/0')

search_box=browser.find_element_by_id('searchtag')
search_box.send_keys(cricketer_name)

click_box=browser.find_element_by_xpath("//div[@class='list-content']//input")
click_box.submit()

current_address=(browser.current_url)



res=requests.get(current_address)

soup=bs4.BeautifulSoup(res.text)
content=soup.select('div span')
print(content[10].text)
final_content=content[10].text


sample_file=open('test.txt','w')
sample_file.write(final_content)
sample_file.close()






