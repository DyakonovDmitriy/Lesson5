def d_arr(n):

    """
    функция которая возвращает список всех делителей числа
    :return:

    """


    int_list=[]
    i=1

    # циклом проверяем все делители числа и добавляем в список

    while i<=n:
        if n%i==0:
            int_list.append(i)
        i+=1

    print(int_list)

    # return(int_list)


