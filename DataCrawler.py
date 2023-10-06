#laays data từ url 2 web
import requests

def get_data_from_techprofit_api():
    url = 'https://api.techprofit.vn/admin/credit/aggregate/route/active-users-by-date-range'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "fromDate": "2023-10-09 00:00:00",
        "toDate": "2023-10-13 00:00:00",
        "domain": "api.techprofit.vn"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # The request was successful
        response_data = response.json()
        data = response_data.get('data')
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


def get_data_from_takeprofit_api():
    url = 'https://api.takeprofit.vn/admin/credit/aggregate/route/active-users-by-date-range'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "fromDate": "2023-10-09 00:00:00",
        "toDate": "2023-10-13 14:30:00",
        "domain": "api.takeprofit.vn"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # The request was successful
        response_data = response.json()
        data = response_data.get('data')
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

