import requests

url = "https://twitter154.p.rapidapi.com/user/tweets"

querystring = {"username":"shahriarshm","limit":"5","include_replies":"false","include_pinned":"false"}

headers = {
	"X-RapidAPI-Key": "2fb86e469dmsh88fe43922238e96p1fdc27jsn719ba5770ad1",
	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# import requests

# url = "https://twitter154.p.rapidapi.com/user/details"

# querystring = {"username":"shahriarshm"}

# headers = {
# 	"X-RapidAPI-Key": "2fb86e469dmsh88fe43922238e96p1fdc27jsn719ba5770ad1",
# 	"X-RapidAPI-Host": "twitter154.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())