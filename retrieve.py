from tranco import Tranco
import numpy as np
from datetime import date, timedelta
import time


def get_full_tranco_list():
    t = Tranco(cache=True, cache_dir='.tranco', account_email="claeysolivier@hotmail.com",
               api_key="bca37554dcd54b78a5592aa4ac3b6d55")
    latest_tranco_list = t.list()
    latest_tranco_array = np.array(latest_tranco_list.top(1000000))
    return latest_tranco_array


def get_majestic_list(d):
    t = Tranco(cache=True, cache_dir='.tranco', account_email="claeysolivier@hotmail.com",
               api_key="bca37554dcd54b78a5592aa4ac3b6d55")
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


def get_all_data():
    start_date = date(2022, 3, 11)
    end_date = date(2023, 3, 11)
    delta = timedelta(days=15)
    date_list = []
    while start_date <= end_date:
        date_list.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta

    list_of_lists = []
    for da in date_list:
        time.sleep(5)
        list_of_lists.append(np.array(get_majestic_list(da)))
    list_of_lists = np.array(list_of_lists)
    return date_list, list_of_lists