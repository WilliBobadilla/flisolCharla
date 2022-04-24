
#author: Williams Bobadilla
#created_at: 22 abr 2022
#edited_by: Williams Bobadilla
#edited_at: 22 abr 2022
#description: bot to comment in youtube videos
# https://questionpro.com/t/AVUojZsRRm

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import sys 


with open('respuestas.txt', 'r') as fil: 
    responses = fil.read().split("\n")
    print(responses)


FORM_LINK = "https://questionpro.com/t/AVUojZsRRm"

driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get(FORM_LINK)

#wait loading of this element
WebDriverWait(driver, 30).until(
	EC.presence_of_element_located((By.ID,"legend_107791229"))
)

div_number = randint(1,3)
print(div_number)
path_one = f"/html/body/div[5]/div[2]/form/div[1]/fieldset[1]/div/div[{div_number}]/label/span[1]"
question_one = driver.find_element(By.XPATH,path_one)
question_one.click()
sleep(1)
#elegimos un texto random 
text_random = responses[randint(0,len(responses)-1)]
print("Texto aleatorio elegido: ", text_random)
question_two = driver.find_element(By.XPATH,"//*[@id='578809235ID']")
question_two.send_keys(text_random)
sleep(1)
done_button = driver.find_element(By.XPATH, "//*[@id='SurveySubmitButtonElement']")
done_button.click()
sleep(3)
driver.close()