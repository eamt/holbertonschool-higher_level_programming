def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    maxi = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > maxi:
            maxi = my_list[i]
        i += 1
    return maxi
