
# package import statement
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp
from api_func import *


otp_key = 'IYMVXFYOF2XHBZZHVCKGUBAF6A'



def login(smartApi:SmartConnect,otp_key:str,client_id:str,pwd:str)->bool:
	"""Performs login to the account and updates the smartapi objext with access, feed, refresh tokens and user ID"""

	totp=pyotp.TOTP(otp_key).now()
	data = smartApi.generateSession(client_id, pwd, totp)
	#print(data)
	if data['message'] == "SUCCESS":
		print("Login successful")
		
	else:
		print(data)

	return data['status']	

def get_profile(smartApi:SmartConnect):
	"""Fecthes the user profile"""
	data = smartApi.getProfile(smartApi.refresh_token)
	if data['message'] == "SUCCESS":
		print("Profile sucessfully feteched")
		
	else:
		print(data['message'])

	return data['data']



def main()-> None:
	print("Running Main")
	api_key = 'kOxXBPji'
	smartApi = SmartConnect(api_key)
	result = login(smartApi,otp_key,"K341951","5991")
	if result:
		print(smartApi.userId)
		# portfolio = get_portfolio(smartApi)
		# display_portfolio(portfolio)
		get_positions(smartApi)


if __name__ == "__main__":
	main()

	