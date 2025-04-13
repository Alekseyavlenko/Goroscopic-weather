import requests

s_city = "Petersburg"
city_id = 0
appid = "буквенно-цифровой APPID"
try:
    res = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key=92b3755806724764b2f93911251304&q={s_city}&aqi=no")
    data = res.json()
    # cities = ["{} ({})".format(d['name'], d['sys']['country'])
    # for d in data['list']]
    # print("city:", cities)
    # city_id = data['list'][0]['id']
    # print('city_id=', city_id)
    print(data)
except Exception as e:
    print("Exception (find):", e)
    pass
