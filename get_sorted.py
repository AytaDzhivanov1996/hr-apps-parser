from course_project.select_sorted import select_sorted


def main():
    user_input = input("Сортировать по цене\nоткрытия (open)\nзакрытия (close)\nмаксимум [high]\nминимум (low)\nобъем (volume):\n")
    user_input_2 = input("Порядок по убыванию (desc) возрастанию [asc]:\n")
    user_input_3 = input("Ограничение выборки [10]:\n")
    user_input_4 = input("Название файла для сохранения результата [dump.csv]:\n")
    if user_input == '':
        sorted_list = select_sorted(sort_columns=['high'], order=user_input_2, limit=int(user_input_3), filename=user_input_4)
    if user_input_2 == '':
        sorted_list = select_sorted(sort_columns=[user_input], order='asc', limit=int(user_input_3), filename=user_input_4)
    if user_input_3 == '':
        sorted_list = select_sorted(sort_columns=[user_input], order=user_input_2, limit=10, filename=user_input_4)
    if user_input_4 == '':
        sorted_list = select_sorted(sort_columns=[user_input], order=user_input_2, limit=int(user_input_3), filename='dump.csv')
    else:
        sorted_list = select_sorted(sort_columns=[user_input], order=user_input_2, limit=int(user_input_3), filename=user_input_4)
    for i in sorted_list:
        print(i)
    return sorted_list


if __name__ == '__main__':
    main()
