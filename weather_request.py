import requests


def pogoda_request(sity, country):
    s_city = f"{sity},{country}"
    city_id = 0
    appid = "буквенно-цифровой APPID"
    try:
        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=92b3755806724764b2f93911251304&q={s_city}&aqi=no&lang=ru")
        data = res.json()
        print(data)
    except Exception as e:
        print("Exception (find):", e)


pogoda_request('Москва', 'Россия')
