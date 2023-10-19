from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import time
import pandas as pd

options = Options()
options.add_argument("--headless=new")
options.add_argument("window-size=1920,1080")


print(r"""\
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀⣀
                ⠀⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣶⡿⢋
                ⠀⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
                ⠀⠹⣿⣿⣿⣿⣶⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
                ⠀⣄⣈⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
                ⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀
                ⠀⠀⣀⣉⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
                ⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢉⣩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀
                ⠒⠶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ .com                                    
                --v1.0  by-imbngy
                """)



website = "https://twitter.com/login"
driver = webdriver.Chrome(options=options)
driver.get(website)


WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, './/input'))
user_log1 = input("Enter your username/email: ")
username = driver.find_element(By.XPATH, './/input').send_keys(user_log1)



login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
login.click()
#check if the username/email is valid
try:
    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(By.XPATH, './/input[@name="password"]'))
    exists = driver.find_elements(By.XPATH, './/input[@name="password"]')
    if exists:
        pass
except:
    print(" ")
    print("Login failed, please try again.")
    driver.quit()
    exit()

WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, './/input[@name="password"]'))
user_log2 = getpass.getpass("Enter your password: ")
password = driver.find_element(By.XPATH, './/input[@name="password"]').send_keys(user_log2)
WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'))
final_log = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
final_log.click()
#check if the login was successful
try:
    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(By.XPATH, './/input[@aria-label="Search query"]'))
    exists = driver.find_elements(By.XPATH, './/input[@aria-label="Search query"]')
    if exists:
        pass
except:
    print(" ")
    print("Login failed, please try again.")
    driver.quit()
    exit()


#-----search mode selection
print(" ")
print("Select a search mode: ")
print("1. Search by keyword")
print("2. Search by user")
print(" ")
search_mode = input("Enter a number: ")
#SEARCH BY KEYWORD
if search_mode == "1":
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, './/input[@aria-label="Search query"]'))
    search = input("Enter a search term: ")
    search_term = driver.find_element(By.XPATH, './/input[@aria-label="Search query"]')
    search_term.send_keys(search)
    time.sleep(1)
    search_term.send_keys(Keys.RETURN)
#SEARCH BY USER
elif search_mode == "2":
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, './/input[@aria-label="Search query"]'))
    search = input("Enter the desired username: ")
    search_term = driver.find_element(By.XPATH, './/input[@aria-label="Search query"]')
    search_term.send_keys(search)
    time.sleep(1)
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, './/div[@data-testid="TypeaheadUser"]'))
    user_found = driver.find_element(By.XPATH, './/div[@data-testid="TypeaheadUser"]')
    user_found.click()
    time.sleep(1)
elif search_mode != "1" or search_mode != "2":
    print("Invalid option, please try again.")
    driver.quit()
    exit()


#scrape the tweets
def get_tweet(element): 
    try:
        WebDriverWait(driver, 10).until(lambda driver: tweet.find_element(By.XPATH, './/span[contains(text(), "@")]'))
        user = element.find_element(By.XPATH, './/span[contains(text(), "@")]').text
        text = element.find_element(By.XPATH, './/div[@lang]').text
        tweets_data = [user, text]
    except:
        tweets_data = ["user", "text"]

    return tweets_data

users = []
texts = []
tweet_ids = set()
scrolling = True
while scrolling:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, './/article[@role="article"]')))
    tweets = driver.find_elements(By.XPATH, './/article[@role="article"]')

    #get the data from the tweets
    for tweet in tweets:
        tweet_list = get_tweet(tweet)
        tweet_id = "".join(tweet_list)
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            users.append(tweet_list[0])
            print(" ")
            print("#############################################")
            print(tweet_list[0])
            texts.append(" ".join(tweet_list[1].split()))
            print(" ".join(tweet_list[1].split()))
            print("#############################################")
    
    #scroll down to load more tweets
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True: 
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        #if new_height == last_height:
        #   scrolling = False
        #    break
        if len(users) > 100:  #change this number to the desired amount of tweets to scrape
            scrolling = False 
            break 
        else:
            last_height = new_height 
            break

driver.quit()

#save the data to a csv file
df_tweets = pd.DataFrame({'user': users, 'text': texts}) 
df_tweets.to_csv('tweets.csv', index=False) 
print("Done!") 