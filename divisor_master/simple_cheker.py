from math import sqrt

def simple_cheker(n):

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

    i=2

    limit=int(sqrt(n))
    if n<2:
        print ('Digit must be more than 2')
        # break
    elif n==2:
        print("it's Prime number")
        # break
    else:
        while i<=limit:
            if n%i==0:
                print('This is composit number')
                break
            else:
                print('Prime number')
            i += 1

    # return(q1)