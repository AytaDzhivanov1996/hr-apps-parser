import csv
from itertools import islice

csv_file = open('../all_stocks_5yr.csv')
reader = csv.DictReader(csv_file)
lst = list(reader)


def select_sorted(**kwargs):
    """функция для сортировки (задается пользователем)"""
    cache = []
    x = kwargs['sort_columns'][0]

    def partition(array, low, high):
        """функция для разделения массива"""
        pivot = array[high][x]
        i = low - 1
        for j in range(low, high):
            if array[j][x] <= pivot:
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quick_sort(array):
        """функция быстрой сортировки"""
        def _quick_sort(objects, low, high):
            """функция с рекурсией"""
            if low < high:
                pi = partition(objects, low, high)
                _quick_sort(objects, low, pi - 1)
                _quick_sort(objects, pi + 1, high)

        _quick_sort(array, 0, len(array) - 1)
        return array
    if len(cache) == 0:
        if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'asc':
            sorted_list = quick_sort(lst)
        if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'desc':
            sorted_list = quick_sort(lst)
            sorted_list.reverse()
        if 'limit' in list(kwargs.keys()) and 'filename' in list(kwargs.keys()):
            limited_sorted_list = list(islice(sorted_list, 0, kwargs['limit']))
            cache.append(limited_sorted_list)
            f = open(f'../{kwargs["filename"]}', 'w')
            f.write(str(limited_sorted_list))
            f.close()
            return limited_sorted_list
    else:
        return cache


def get_by_date(**kwargs):
    """функция для поиска по дате и названию компании"""
    srt_lst = select_sorted(sort_columns=['high'], order='asc')
    for d in srt_lst:
        if kwargs['date'] == d['date'] and kwargs['name'] == d['Name']:
            f = open(f'../{kwargs["filename"]}', 'w')
            f.write(str(d))
            f.close()
            return d
