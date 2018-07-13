import json

data = {}

with open('config.json') as json_data_file:
    data = json.load(json_data_file)



coinex_api_id = data['coinex_api_id']

coinex_api_key = data['coinex_api_key']

partial_ratio =  data['partial_ratio']

bid_ask_spread = data['bid_ask_spread']

wave_ratio =  data['wave_ratio']

market = data['market']

goods = data['goods']

money = data['money']

wait_order = data['wait_order']

stop_threshold = data['stop_threshold']

first_submit = data["first_submit"]