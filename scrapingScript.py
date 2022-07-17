from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import csv  
from selenium.webdriver.support import expected_conditions as EC
refence url-"https://www.skiresort.info/ski-resort/les-3-vallees-val-thorensles-menuiresmeribelcourchevel/"
urlslist=['list of urls']
data=[]
aprice=""
yprice=""
cprice=""
header=['Resort Name','URL','Percentage of Beginner Slopes','Percentage of Inter Slopes','Percentage of Advanced Slopes','Total Ski Slopes','Elevation','Adult Pass Cost','Child Pass Cost','Youth Pass Cost','Reviews']
with open('resortInfo.csv', 'a+', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    

for i in urllists:
    
    driver = uc.Chrome()
    driver.get(i)
    try:
        sdata = driver.find_element(By.ID,"selSlopetot")
        try:
            Slopes=sdata.text
            slopeinfo=Slopes.split(":")
            totalslope=slopeinfo[1]
        except (ElementClickInterceptedException,ElementNotInteractableException):
            totalslope="Not Available"
    except:
        totalslope="Not Available"
    
#     Slopes=driver.find_element(By.ID,"selSlopetot").text
    try:
        ski = driver.find_element(By.CLASS_NAME,"fn")
        try:
            skiName=ski.text
        except (ElementClickInterceptedException,ElementNotInteractableException):
            aprice="Not Available"
    except:
        aprice="Not Available"
    url=driver.current_url
#     skiName= driver.find_element(By.CLASS_NAME,"fn").text
    try:
        bigner = driver.find_element(By.ID,"selBeginner")
        try:
            bignerslope=bigner.text
        except (ElementClickInterceptedException,ElementNotInteractableException):
            bignerslope="Not Available"
    except:
        bignerslope="Not Available"
    intermediate=driver.find_element(By.ID,"selInter").text
    difficult = driver.find_element(By.ID,"selAdv").text
    elevationinfo= driver.find_element(By.ID,"selAlti").text

    try:
        adult = driver.find_element(By.ID,"selTicketA")
        try:
            aprice=adult.text
        except (ElementClickInterceptedException,ElementNotInteractableException):
            aprice="Not Available"
    except:
        aprice="Not Available"
    try:
        childpass = driver.find_element(By.ID,"selTicketC")
        try:
            cprice=childpass.text
        except (ElementClickInterceptedException,ElementNotInteractableException):
            cprice="Not Available"
    except:
        cprice="Not Available"

    try:
        youth = driver.find_element(By.ID,"selTicketY")
        try:
            yprice=youth.text
        except (ElementClickInterceptedException,ElementNotInteractableException):
            yprice="Not Available"
    except:
        yprice="Not Available"

    reviews=driver.find_element(By.ID,"selRating").text
    if(aprice!="" and cprice!="" and yprice!=""):
        data=[skiName,url,totalslope,bignerslope,intermediate,difficult,elevationinfo,aprice,cprice,yprice,reviews]
        print(data)
    elif(cprice!="" and aprice!="" and  yprice ==""):
        data=[skiName,url,totalslope,bignerslope,intermediate,difficult,elevationinfo,aprice,cprice,yprice,reviews]
        print(data)

    elif(yprice!="" and aprice!="" and cprice==" "):
        data=[skiName,url,totalslope,bignerslope,intermediate,difficult,elevationinfo,aprice,cprice,yprice,reviews]
        print(data)

    elif(yprice!="" and aprice=="" and cprice!=" "):
        data=[skiName,url,totalslope,bignerslope,intermediate,difficult,elevationinfo,aprice,cprice,yprice,reviews]
        print(data)
    
    time.sleep(2)
    with open('resortInfo.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    with open('resortInfo.csv', 'r+') as fd:
        lines = fd.readlines()
        fd.seek(0)
        fd.writelines(line for line in lines if line.strip())
        fd.truncate()
   
    driver.close()
    