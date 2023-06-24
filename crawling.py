from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import re

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 브라우저 생성
browser = webdriver.Chrome(executable_path='/User/choiboyoung/Documents/chromedriver', options=chrome_options)

# 웹사이트 열기
browser.get('https://m.kinolights.com/discover/explore')
browser.implicitly_wait(3) # 로딩이 끝날 때까지 5초까지 기다려줌

# 넷플릭스 클릭
netflix_button = browser.find_element(By.XPATH, '/html/body/div/div/div/main/section/div[2]/div/div/div/div[2]/button')
actions = ActionChains(browser).move_to_element(netflix_button).pause(1).click()
actions.perform()

time.sleep(1)

titles = browser.find_elements(By.CSS_SELECTOR, '.MovieItem.grid > a')
time.sleep(1)

# 작품 url 가져오기
titles_href = []
for title in titles:
    link = title.get_attribute('href')
    titles_href.append(link)
print(titles_href)
    
n1 = len(titles_href)
for i1 in range(0, n1+1):
    browser.get(titles_href[i1])
    
    time.sleep(1)  
    
    try:
        review_more_button = browser.find_element(By.XPATH, '//*[@id="synopsis"]/section/button')
   
        # 리뷰가 50개 이상일 경우
        if "리뷰" in review_more_button.text:
            n = int(re.findall('\d+', review_more_button.text)[0])
            
            if n >= 50:
                # 파일 생성
                filename = browser.find_element(By.CSS_SELECTOR, '.title-kr').text
                f = open(r"/Users/choiboyoung/소융캡/넷플릭스_리뷰_크롤링/" + filename + ".csv", 'w', encoding='utf-8-sig', newline='')
                csvWriter = csv.writer(f)
                time.sleep(1)
                
                with open(r"/Users/choiboyoung/소융캡/넷플릭스_리뷰_크롤링/" + filename + "_character.txt", 'w', encoding='utf-8-sig') as g:
                
                    # 극중 이름
                    character_list = []
                        
                    characters = browser.find_elements(By.CSS_SELECTOR, '.person > .character')
                    for i in characters:
                        if i.text != '감독':
                            character_list.append(i.text)
                            #보통 외국이름
                            if len(i.text.split()) > 1:
                                for char in i.text.split():
                                    character_list.append(char)
                                    
                            #보통 한국이름    
                            if len(i.text) == 3 and ' ' not in i.text:
                                name = i.text[1:]
                                character_list.append(name)
                            elif len(i.text) ==2 and ' ' not in i.text:
                                name = i.text[1]
                                character_list.append(name)
                            elif len(i.text) == 4 and ' ' not in i.text:
                                name = i.text[1:]
                                character_list.append(name)
                                    
                    for word in character_list:
                        g.write(str(word))
                        g.write('\n')
                    g.close

                # '리뷰더보기' 클릭
                
                review_more_button.send_keys(Keys.ENTER)
                time.sleep(1)

                # 스크롤 전 높이
                before_h = browser.execute_script("return window.scrollY")

                # 무한 스크롤
                while True:
                    # 맨 아래로 스크롤 내리기
                    browser.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.END)
                                
                    # 스크롤 사이 페이지 로딩 시간
                    time.sleep(1)
                                    
                    # 스크롤 후 높이
                    after_h = browser.execute_script("return window.scrollY")
                                    
                    if after_h == before_h:
                        break
                    before_h = after_h

                time.sleep(2)

                # 스포 버튼 '확인'
                spolist = browser.find_elements(By.CSS_SELECTOR, '.has-spoiler > button')
                for spo in spolist:
                    spo.send_keys(Keys.ENTER)
                    time.sleep(1)

                    # alert창 끄기
                    WebDriverWait(browser, 3).until(EC.alert_is_present())
                    alert = browser.switch_to.alert
                    alert.accept()
                    time.sleep(1)
                    
                # 리뷰 링크 가져오기    
                reviews = browser.find_elements(By.CSS_SELECTOR, '.review-title')
                review_href = []   
                for review in reviews:
                    root = review.find_element(By.XPATH, '..')
                    href = root.get_attribute('href')
                    review_href.append(href)
                print(review_href)

                n2 = len(review_href)
                    
                # 리뷰 내용
                contents = []
                for i2 in range(n2):
                    browser.get(review_href[i2])
                        
                    time.sleep(1)
                        
                    try:
                        title = browser.find_element(By.CSS_SELECTOR, '.review-title').text
                        content = browser.find_element(By.CSS_SELECTOR, '.contents > p').text
                        score = browser.find_element(By.CSS_SELECTOR, '.user-star-score').text
                                                    
                    except:
                        title = browser.find_element(By.CSS_SELECTOR, '.review-title').text
                        content = browser.find_element(By.CSS_SELECTOR, '.review-content.fullReview').text
                        score = browser.find_element(By.CSS_SELECTOR, '.user-star-score').text
                            
                    contents.append([title, content, score])
                    time.sleep(1)
                    
                columns_name = ["title", "content", "score"]    
                csvWriter.writerow(columns_name)                        
                csvWriter. writerows(contents)
                f.close()
                
    except:
        pass