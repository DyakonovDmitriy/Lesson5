def max_devider(n):
    """
    функция определения максимального делителя
    :param n: передаваемое число
    :return: возвращает максимальный делитель
    """

    i=1
    max_dev=1

    for i in range(n-1,1,-1):
        if (n%i==0):
            if (max_dev<i):
                max_dev=i


    print(max_dev)

    # return max_dev