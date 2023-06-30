import requests

def get_data_from_api():
    url = 'https://api.takeprofit.vn/admin/credit/aggregate/route/active-users-by-date-range'
    headers = {
        'Content-Type': 'application/json',
        'X-Authorization': '',
        'Authorization': 'Bearer keyb70Fect3eWx2tY'
    }
    data = {
        "fromDate": "2023-06-27 00:00:00",
        "toDate": "2023-06-29 00:00:00"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        return response.status_code
