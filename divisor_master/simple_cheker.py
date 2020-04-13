from math import sqrt

def F1(n):

    '''
    функция проверки просто n число или сложное
    :param n: число
    :return: число
    '''

    # проверяем условие больше нуля но меньше 1000
    # if (n<0) and (n>1000):
    #     print('wrong range')
    #     quit()
    #


    # проверяем число простое оно или нет
    if n<2:
        print ('Digit must be more than 2')
        quit()
    elif n==2:
        print("it's simple digit")
        quit()

    i=2

    limit=int(sqrt(n))
    while i<=limit:
        if n%i==0:
            print('This is composit number')
            quit()
        i+=1

    print('Prime number')

    # return(q1)