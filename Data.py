'''import requests

def get_data_from_api():
    url = 'https://api.takeprofit.vn/admin/credit/aggregate/route/active-users-by-date-range'
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "fromDate": "2023-07-01 00:00:00",
        "toDate": "2023-07-28 00:00:00",
        "domain": "api.takeprofit.vn"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # The request was successful
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

print(get_data_from_api())'''