import http

from selenium import webdriver

def test_scores_service(app_url):
    driver = webdriver.Chrome(executable_path="/Users/bellamarkovitz/Downloads/chromedriver 6")
    driver.get("http://0.0.0.0:8777/")
    element_score = int(driver.find_element_by_id("score").text)
    if element_score > 0 and element_score < 1000 :
        return True
    else:return False

def main_function():
    test = test_scores_service("http://0.0.0.0:8777/")
    if test == False:
        return "0"
    else:return "-1"

main_function()


