#!/usr/bin/python3
def weight_average(my_list=[]):

    if my_list is None or my_list == []:
        return (0)



        result = 0

        divider = 0

        for x, y in my_list:

            result += x * y

            divider += y



        return (result/divider)
