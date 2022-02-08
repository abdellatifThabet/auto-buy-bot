from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import time, sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--incognito")
#chrome_options.headless = True
chrome_options.add_argument("--disable-notifications")

#chrome_options.add_argument("--disable-dev-shm-usage")
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import datetime
import os



def loggingin():
    driver.get(url)

    #####*************************************************** LOGIN ******************************************************************************
    #open new window to login
    driver.execute_script("window.open('" +login_url +"');")
    # switch to new window
    driver.switch_to.window(driver.window_handles[1])
    #connexion to account
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[4]/div[1]/div[1]/div/form/div[1]/div[2]/input"))).send_keys(email)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[4]/div[1]/div[1]/div/form/div[2]/div[2]/input"))).send_keys(passwd)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[4]/div[1]/div[1]/div/form/div[3]/button"))).click()
    sleep(0.5)
    ### the cart needs to be empty
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/a[1]"))).click()
    sleep(0.5)
    ### the cart needs to be empty
    remove = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    for x in range(1,len(remove)):
        remove[x].clear()
        remove[x].send_keys("0")

    #********************************************
    driver.switch_to.window(driver.window_handles[0])
    #####*************************************************** LOGIN ******************************************************************************
    return


def auto_buy_bot():
    driver.refresh()
    ## get all products and add to cart
    products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div[2]/div/div[4]/div[2]/div/div")))
    
    if (len(products) <2):
        return
    #file = open("spain_log.txt","a")
    attempt_start = datetime.datetime.now()
    file.write("products detected on : "+str(attempt_start))
    file.write("\n")
    
    for i, product in enumerate(products):

        if (i==0):
	        continue

        stock =  product.find_element_by_xpath("div[1]/div[2]").text
        prod_name =  product.find_element_by_xpath("div[2]/a/div[1]").text
        ## get all available prods
        num_available = stock.split("x",1)[1] 
        file.write(str(num_available)+" units added for "+str(prod_name))
        file.write("\n")
        ## click add to cart if exists
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[4]/div[2]/div/div['+str(i+1)+']/div[3]/div[2]/a/div'))).click()
        except:
            pass
        wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[4]/div[2]/div/div['+str(i+1)+']/div[3]/div[2]/div/div/input'))).send_keys(num_available)  
    ## now we add products to cart
    ## click on cart

    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div/a[1]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div/div/div[2]/a/div"))).click()

    select = Select(wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/select'))))
    select.select_by_visible_text(buisiness)
    ##Check terms and conditions
    element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div[2]/div[3]/div[2]/div/label")))
    driver.execute_script("arguments[0].click();", element) 
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div/div/div[2]/a/div"))).click()
    file.write("above portugal containers purchased !!")
    sleep(1)
    file.write("\n")
    attempt_end = datetime.datetime.now()
    file.write("Attempt ended on : "+str(attempt_end))
    file.write("\n")
    file.write("-----------------------------------------------------------------")
    file.write("\n")
    file.close()
    driver.get(url)
    ## remove all added to the cart products in case of fail!
    return




try:
    
    print("logging in...")
    
    

    driver = webdriver.Chrome(executable_path='/home/ubuntu-vm/last-release/chromedriver', options=chrome_options)
    wait = WebDriverWait(driver, 2)
    login_url = r'https://maerskcontainersales.com/signin'
    url = 'https://maerskcontainersales.com/products?countries=PT&conditions=DAMAGE,RECYCLE&types=20%27%20Dry%20Standard,40%27%20Dry%20High,40%27%20Dry%20Standard,45%27%20Dry%20High,20%27%20Reefer%20Standard,40%27%20Reefer%20High&cities=PTSIE,PTLEX,PTLIS,PTRHS&sites=PTLEX02,PTLEXTM,PTLEXRL,PTBBLAL,PTBBLAC,PTLIS04,PTLIS05,PTLISTM,PTRHSTV,PTSIETM,PTSIE04'
    email = 'africafrutexport@yahoo.es'
    passwd = '87654321'
    buisiness = 'CHRISTIAN ROJO UNIPESSOAL LDA'

    loggingin()

    print("fetching portugal containers ...")

    while(True):
        file = open("/home/ubuntu-vm/last-release/portugal_log.txt","a")
        auto_buy_bot()
        
        sleep(2)



except:
    try:
        driver.close()
        driver.quit()
    except:
        pass
    os.system("python /home/ubuntu-vm/last-release/portugal-auto-buy.py")





