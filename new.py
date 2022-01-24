# article = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/h2/a")
article = driver.find_elements_by_xpath('//h2[@class="col-sm-6"]')

print(article)