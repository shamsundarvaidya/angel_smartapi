
# package import statement
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp

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

def get_portfolio(smartApi:SmartConnect)-> []:
	data = smartApi.holding()
	holdings = []
	if data['message'] == "SUCCESS":
		holding_data = data['data']
		
		for entry in holding_data :
			item = {}
			item['tradingSymbol'] = entry['tradingSymbol']
			item['quantity'] = entry['quantity']
			item['symboltoken'] = entry['symboltoken']
			item['averageprice'] = entry['averageprice']
			item['ltp'] = entry['ltp']
			item['profitandloss'] = entry['profitandloss']

			holdings.append(item)
	else: 

		print(data['message'])


	return holdings




if __name__ == "__main__":
	api_key = 'kOxXBPji'
	smartApi = SmartConnect(api_key)
	result = login(smartApi,otp_key,"K341951","5991")
	if result:
		print(smartApi.userId)
	portfolio = get_portfolio(smartApi)

	print(portfolio)

	