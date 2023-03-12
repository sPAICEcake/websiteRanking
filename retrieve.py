from tranco import Tranco
import numpy as np
from datetime import date, timedelta

t = Tranco(cache=True, cache_dir='.tranco', account_email="claeysolivier@hotmail.com", api_key="bca37554dcd54b78a5592aa4ac3b6d55")

def get_full_tranco_list():

    latest_tranco_list = t.list()
    latest_tranco_array = np.array(latest_tranco_list.top(1000000))
    return latest_tranco_array


def get_majestic_list(d):
    c = t.configure(
        {
            'providers': ['majestic'],
            'startDate': d,
            'endDate': d,
            "combinationMethod": "dowdall",
            'listPrefix': 'full',
            'filterPLD': 'off'
        }
    )
    latest_majestic_list = t.list(list_id=c[1])
    latest_majestic_array = np.array(latest_majestic_list.top(1000000))
    return latest_majestic_array

start_date = date(2022, 3, 11)
end_date = date(2023, 3, 11)
delta = timedelta(days=15)
date_list = []
while start_date <= end_date:
    date_list.append(start_date.strftime("%Y-%m-%d"))
    start_date += delta
print(date_list)

for d in date_list