from math import sqrt
def max_simple_devider(n):
    """
    функция которая опеределяет максимальный простой делитель числа
    :param n: число подаваемое на вход
    :return: максимальный простой делитель числа
    """


    print("Простые:", end = " ")
    for i in range(n-1, 1, -1):
        is_simple = 0 # Счётчик
        if (n% i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    is_simple = is_simple + 1 # Увеличиваем, если находим делитель
            if (is_simple == 0): # Если делителей не было найдено, выводим
                print("Максимально простой делитель ",i, end = " ")
                quit()





# попытался сделать то же самое но циклом while но почему-то не стартануло
# не понимаю почему

#n=63
# i=1
# j=1
#
# divider_list=[]
# simple_devider=[]
#
# while i<=n:
#     if n%i==0:
#         while j<i:
#             if i%j==0:
#                 count=count+1
#         j+=1
#         print(i)
#     i+=1
#
# while i<=n:
#     if n%i==0:
#         divider_list.append(i)
#     i+=1
#
# a=divider_list[1:-1]
# print(a)



