from selenium import webdriver
import time
import os

refresh=input("Enter refresh time in seconds:")
count=input("how many views do you want:")


for i in range(int(count)):
	os.system('sudo ifconfig eth0 down')
	os.system('sudo ifconfig eth0 159.203.189.19'+str(i))
	os.system('sudo ifconfig eth0 up')
	driver = webdriver.Chrome()
	driver.get("Put Your Urla")
	time.sleep(int(refresh))
	driver.quit()
	


