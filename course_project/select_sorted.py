import pandas as pd
from itertools import islice
from functools import lru_cache

df = pd.read_csv('all_stocks_5yr.csv')
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
df.fillna(0, inplace=True)
lst = df.to_dict('records')


@lru_cache(maxsize=10)
def select_sorted(**kwargs):
    """функция для сортировки (задается пользователем)"""
    x = kwargs['sort_columns']

    def partition(array, low, high):
        """функция для разделения массива"""
        pivot_index = low
        pivot = array[pivot_index][x]
        while low < high:
            while low < len(array) and array[low][x] <= pivot:
                low += 1
            while array[high][x] > pivot:
                high -= 1
            if low < high:
                array[low], array[high] = array[high], array[low]
        array[high], array[pivot_index] = array[pivot_index], array[high]
        return high

    def quick_sort(array):
        """Функция быстрой сортировки"""

        def _quick_sort(objects, low, high):
            """Внутренняя функция, вызываемая рекурсивно"""
            if low < high:
                pi = partition(objects, low, high)
                _quick_sort(objects, low, pi - 1)
                _quick_sort(objects, pi + 1, high)

        _quick_sort(array, 0, len(array) - 1)
        return array

    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'asc':
        sorted_list = quick_sort(lst)
    if 'sort_columns' in list(kwargs.keys()) and kwargs['order'] == 'desc':
        sorted_list = quick_sort(lst)
        sorted_list.reverse()
    if 'limit' in list(kwargs.keys()) and 'filename' in list(kwargs.keys()):
        limited_sorted_list = list(islice(sorted_list, 0, kwargs['limit']))
        f = open(f'results/{kwargs["filename"]}', 'w')
        f.write(str(limited_sorted_list))
        f.close()
        return limited_sorted_list
    return sorted_list


@lru_cache(maxsize=10)
def get_by_date(**kwargs):
    """Функция поиска по дате и названию компании"""
    data = select_sorted(sort_columns='date', order='asc')
    named_data = []
    for el in data:
        if el['Name'] == kwargs['name']:
            named_data.append(el)

    def binary_search(array, element, start, end):
        """Функция бинарного поиска"""
        if start > end:
            return array[-1]
        mid = (start + end) // 2
        if element == array[mid]['date']:
            return array[mid]
        if element < array[mid]['date']:
            return binary_search(array, element, start, mid - 1)
        else:
            return binary_search(array, element, mid + 1, end)

    if kwargs['date'] == '':
        f = open(f'results/{kwargs["filename"]}', 'w')
        f.write(str(named_data))
        f.close()
        return named_data
    if kwargs['name'] != '':
        data_found = binary_search(named_data, kwargs['date'], 0, len(named_data))
        f = open(f'results/{kwargs["filename"]}', 'w')
        f.write(str(data_found))
        f.close()
        return data_found
    else:
        one_day_data = []
        for elem in data:
            if elem['date'] == kwargs['date']:
                one_day_data.append(elem)
        f = open(f'results/{kwargs["filename"]}', 'w')
        f.write(str(named_data))
        f.close()
        return one_day_data
