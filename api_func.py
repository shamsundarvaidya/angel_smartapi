from SmartApi import SmartConnect

def get_portfolio(smartApi:SmartConnect)-> []:
	data = smartApi.holding()
	holdings = []
	if data['message'] == "SUCCESS":
		holding_data = data['data']
		
		for entry in holding_data :
			item = {}
			item['tradingsymbol'] = entry['tradingsymbol']
			item['quantity'] = entry['quantity']
			item['symboltoken'] = entry['symboltoken']
			item['averageprice'] = entry['averageprice']
			item['ltp'] = entry['ltp']
			item['profitandloss'] = entry['profitandloss']

			holdings.append(item)
	else: 
		print(f"Failed to fetch holdings due to {data['message']}")		


	return holdings

def get_positions(smartApi:SmartConnect)-> []:
	data = smartApi.position()
	if data['message'] == "SUCCESS":
		positions_data = data['data']
		for entry in positions_data:
			print(entry)
	else:
		print(f"Failed to fetch positions due to {data['message']}")	

def display_portfolio(holdings:[])-> None:
	print(f'Stock \t\t PnL')
	total = 0
	for item in holdings:
		print(f"{item['tradingsymbol']} \t {item['profitandloss']}")
		total = total + item['profitandloss']
	print("-" * 20)
	print(f"Total \t\t {total}")