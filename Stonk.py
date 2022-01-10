import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
options = Options()
import os
import subprocess
from os import system, name 
from time import sleep 
import pyautogui
import webbrowser
from decimal import *
def currentstockpercent():
	global ptn
	global negpos
	global percentnum
	
	
	#url = ("https://ethereumprice.org/live/")
	url = ("https://www.coinbase.com/price/ethereum")
	options.headless = True
	browser = webdriver.Firefox(options=options)
	browser.get(url)


	#percentnum = browser.find_element_by_class_name("percent")
	percentnum = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/main/div/section[2]/div/div/div[2]/div[8]/span')
	percentnum = percentnum.text
	percentnum = str(percentnum)
	negpos = (percentnum[0])
	#ptn = (percentnum[1:])
	ptn = (percentnum[:-1])
	




	


	print(percentnum)
	browser.quit()

	return percentnum
	return ptn
	return negpos
	
#------------------------------------------------------------------------
#Define variables to be used
sold = 0
bought = 0
btradelist = "Sold Stocks this many times: "
stradelist = "Bought Stocks this many times: "

#Start and end with money in Ethereum
ab = 0

#Determine were the money will start
currentstockpercent()
ptn = Decimal(ptn)
arkpath = (ptn) - Decimal(0.50)
print(arkpath)
if ptn <= Decimal(-0.50) :
	ab = 1
	print ("ab = 1")
if ptn >= Decimal(0.50) :
	ab = 0
	print ("ab = 0")


while True:
	#put time wait thing right here if you want
	#clear()
	#sleep(1200)
	print (stradelist)
	print (btradelist)
	currentstockpercent()
	ptn = float(ptn)
	btradelist = "Sold Stocks this many times: "
	stradelist = "Bought Stocks this many times: "
	

	
	if negpos == "-" :
	 print("the stock is negative")
	 if ptn <= -0.50 :
	  print("the stock is less than 0.5%")
	  if ab == 1 :
	   print("I have not already bought stocks soooo")
	   print("buying stocks")
	   ab = 0
	   bought = bought + 1
	   btradelist = btradelist + str(bought)
	   print("Buying Ethereum")
	  
	
	if negpos == "+" :
	 print("The stock is positive")	
	 if ptn >= 0.50 :
	  ("The stock is up more than 0.5%")
	  if ab == 0 :
	   print("I have not already sold stocks sooooo")
	   print("selling stocks")
	   ab = 1
	   sold = sold + 1
	   stradelist = stradelist + str(sold) 
	   print("Selling Ethereum")
	  
	
