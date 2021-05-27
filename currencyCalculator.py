import requests

api_key = "your_api_key"

url = "http://data.fixer.io/api/latest?access_key=" + api_key

f_money = input("First Currency :")
s_money = input("Second Currency :")
money = int(input("quantity : "))

response = requests.get(url)
info = response.json()
f_value = info["rates"][f_money]
s_value = info["rates"][s_money]
print((s_value / f_value) * money)
