from selenium import webdriver
import time

#Connect to website
chrome_driver_path = "G:\Learning Python\Github\Repository\Cookie_clicker\chromedriver.exe"       #path for driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Variables
cookie = driver.find_element_by_id("cookie")
upgrades = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in upgrades]
Upgrades_dict = {}
Upgrades_price = driver.find_elements_by_css_selector("#store b")
Begin_time = time.time()
#5sec break
Time_checkpoint = time.time() + 5


while True:
    cookie.click()

    #Statement after we check for the upgrades
    if time.time() > Time_checkpoint:

        #Get all upgrades b tags
        Upgrades_price = driver.find_elements_by_css_selector("#store b")
        item_prices = []    #Reset list

        #Convert <b> text into an integer price and add it to the list
        for price in Upgrades_price:
            if price.text != "":
                cost = int(price.text.split("- ")[1].replace(",", ""))
                item_prices.append(cost)

        #Get Upgrades id's to theirs cost
        for n in range(len(item_prices)):
           Upgrades_dict[item_prices[n]] = item_ids[n]

        #Get current money in pocket
        money = int(driver.find_element_by_id("money").text.replace(",", ""))
        Affordable_upgrades = {}

        #Find upgrades that we can afford
        for n in range(len(item_prices)):
            if money > item_prices[n]:
                Affordable_upgrades[item_prices[n]] = item_ids[n]

        #Buy the most expensive Upgrade
        highest_price_affordable_upgrade = max(Affordable_upgrades)
        driver.find_element_by_id( Affordable_upgrades.get(highest_price_affordable_upgrade) ).click()

        #Show curretn passive cooki income
        income = driver.find_element_by_id("cps").text
        Passed_time = time.time() - Begin_time
        print(f"Time: {Passed_time}, income: {income}")


        #Reset timer
        Time_checkpoint = time.time() + 5
