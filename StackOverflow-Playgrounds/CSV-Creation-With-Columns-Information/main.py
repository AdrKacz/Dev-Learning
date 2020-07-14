import csv

mylist = ['item1 : server1 server2 server3 server4', 'item2 : server2, server5, server6', 'item3 :' , 'item4 : server11 server12 server13']


mylist_split = [item.replace(':', '').replace(',','').split() for item in mylist]

with open("my_csv_file.csv", 'w', newline='') as csv_file:
	writer = csv.writer(csv_file, delimiter='|', quotechar=' ', quoting=csv.QUOTE_ALL)

	_max_row = max([len(item) for item in mylist_split])
	for i in range(_max_row):
		row = list()
		for item in mylist_split:
			if len(item) > i:
				row.append(item[i])
			else:
				row.append('')
		print(row)
		writer.writerow(row)