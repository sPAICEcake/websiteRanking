import numpy as np
import csv

from retrieve import get_all_data, get_majestic_list


def compare(d1, d2, list1, list2):
    header = ['naam', 'stijgingspercentage', 'verschil', 'huidige_ranking']
    f = open(d1 + "_ranking_" + d2 + ".csv", "w")
    writer = csv.writer(f)
    writer.writerow(header)
    for index1, entry in enumerate(list1):
        if entry in list2:
            index2 = np.where(list2 == entry)[0][0]
            if index2 == 0:
                percentage = 0
            else:
                percentage = - float((index2-index1)/index2) * 100
            if percentage > 0.0:
                out = [str(entry), percentage,int(index1-index2), index1]
                writer.writerow(out)
    f.close()

# all_data = get_all_data()
# all_dates = all_data[0]
# all_lists = all_data[1]
# most_recent_l = all_lists[0]
# most_recent_d = all_dates[0]
#
# for i in range(1, len(all_lists)):
#    compare(most_recent_d, all_dates[i], most_recent_l, all_lists[i])

l1 = get_majestic_list('2023-03-11')
l2 = get_majestic_list('2023-03-06')
compare('2023-03-11', '2023-03-06', l1, l2)
