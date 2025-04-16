import requests


def pogoda_request(sity, country):
    s_city = f"{sity},{country}"
    try:
        res = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key=92b3755806724764b2f93911251304&q={s_city}&aqi=no&lang=ru")
        data = res.json()
        return data
    except Exception as e:
        return str(f"Exception (find):, {e}")



