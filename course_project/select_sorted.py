import csv
from itertools import islice

csv_file = open('../all_stocks_5yr.csv')
reader = csv.DictReader(csv_file)


def select_sorted(**kwargs):
    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'desc':
        sorted_list = sorted(reader, key=lambda row: row[kwargs['sort_columns']], reverse=False)
    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'asc':
        sorted_list = sorted(reader, key=lambda row: row[kwargs['sort_columns']], reverse=True)
    if 'limit' in list(kwargs.keys()):
        limited_sorted_list = list(islice(sorted_list, 0, kwargs['limit']))
    if 'filename' in list(kwargs.keys()):
        f = open('../dump.csv', 'w')
        f.write(str(limited_sorted_list))
        f.close()
        return limited_sorted_list


data = select_sorted(sort_columns='high', order='asc', limit=10, filename='dump.csv')
for i in data:
    print(i)
csv_file.close()
