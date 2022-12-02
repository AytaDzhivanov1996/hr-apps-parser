from course_project.select_sorted import select_sorted, get_by_date


def main():
    user_input = input("Дата в формате yyyy-mm-dd [all]: ")
    user_input_2 = input("Тикер [all]: ")
    user_input_3 = input("Файл [dump.csv]: ")
    if user_input_3 == '':
        data = get_by_date(date=user_input, name=user_input_2, filename='dump.csv')
    else:
        data = get_by_date(date=user_input, name=user_input_2, filename=user_input_3)
    return data


if __name__ == '__main__':
    print(main())
