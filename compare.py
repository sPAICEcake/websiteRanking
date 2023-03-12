import numpy as np

from retrieve import get_all_data

all_lists = np.flip(get_all_data())
f = open("outputfile.txt", "w")

def compare(list1, list2):
    for index1, entry in enumerate(list1):
        index2 = np.where(list2 == entry)
        percentage = - (index2-index1)/index2
        out = "naam: " + entry + " , stijgingspercentage: " + percentage + " , verschil" + str(index2-index1) + " , huidige ranking: " + str(index1)
        f.write(out + "\n")

most_recent = all_lists[0]
for i in range(1, len(all_lists)):
    compare(most_recent, all_lists[i])
f.close()


