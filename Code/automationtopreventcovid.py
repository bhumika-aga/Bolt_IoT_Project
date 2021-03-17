*PYTHON CODE FOR AUTOMATION*
import requests
import json
import configuration_py
import time

from boltiot import Bolt

people=0
count=0

mybolt = Bolt (configuration_py.bolt_api_key, configuration_py.bolt_device_id)

def send_telegram_message(message):
	url = "https://api.telegram.org/"+ config.telegram_bot_id + "/sendMessage"
	data = {
		"chat_id": config.telegram_chat_id,
		"text": message
		}
	try:
		response=requests.request(
			"POST",
			url,
			param=data
			)
		print("This is the Telegram url")
		print(url)
		print("This is the Telegram response")
		print(response.text)
		telegram_data = json.loads(response.text)
		return telegram_data[ok]
	except Exception as e:
		print("An error occurred in sending the alert message via Telegram")
		print(e)
		return False

while True:
	try:
		#COUNTING NUMBER OF PEOPLE IN THE ROOM
		response=mybolt.digitalRead ('1')
		data=json.loads(response)
		if data['value']==0:
			people=people+1
		response=mybolt.digitalRead ('4')
		data=json.loads(response)
		if data['value']==0:
			people=people-1
		if people<0:
			people=0
		if people>0:
			response=mybolt.digitalWrite('3','HIGH')
		print("Number of people in room:"+str(people))
		
		#ALERT FOR OVERCROWDING
		if people>5:
			response=mybolt.digitalWrite ('0','HIGH')
			print(response)
			print("Requesting Telegram to send message for overcrowding")
			message = ("ALERT!", "MORE THAN 5 PEOPLE IN ROOM.STOP OVERCROWDING. MAINTAIN SOCIAL DISTANCING")
			response_text = json.loads(response.text)
			print("Response from Telegram:" + str(response_text['message']))
			
		#REMINDER FOR HAND SANITIZING
		if count%3600==0:
			response=mybolt.digitalWrite ('0','HIGH')
			print("SANITIZE/WASH YOUR HANDS...STAY SAFE!")
			time.sleep(5)
		count=count+60
	except Exception as e:
		print ("Error occured: Below are the details")
		print (e)
		time.sleep(60)