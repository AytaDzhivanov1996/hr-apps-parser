from course_project.select_sorted import select_sorted


def main():
    user_input = input("Сортировать по цене\nоткрытия (1)\nзакрытия (2)\nмаксимум [3]\nминимум (4)\nобъем (5):\n")
    user_input_2 = input("Порядок по убыванию (desc) возрастанию [asc]:\n")
    user_input_3 = input("Ограничение выборки [10]:\n")
    user_input_4 = input("Название файла для сохранения результата [dump.csv]:\n")
    command_dict_1 = {'1': 'open', '2': 'close', '3': 'high', '4': 'low', '5': 'volume'}
    command_dict_2 = {'1': 'desc', '2': 'asc'}
    if user_input_3 == '':
        sorted_list = select_sorted(sort_columns=command_dict_1[user_input], order=command_dict_2[user_input_2], limit=10, filename=user_input_4)
    else:
        sorted_list = select_sorted(sort_columns=command_dict_1[user_input], order=command_dict_2[user_input_2], limit=int(user_input_3), filename=user_input_4)
    for i in sorted_list:
        print(i)
    return sorted_list


if __name__ == '__main__':
    main()
