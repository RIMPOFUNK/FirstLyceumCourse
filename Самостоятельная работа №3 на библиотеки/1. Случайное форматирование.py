import random as rand


def random_format(string, **kwargs):
    ret = ''
    tmp = ''

    for i in string:
        if tmp in kwargs:
            ret += str(sum(rand.sample(kwargs[tmp], 2)))
            tmp = ''
        if i in '*/%+-=???':
            ret += i
        else:
            tmp += i
    return ret


print(random_format('first+second+first*second=???', first={1, 2, 3}, second={4, 5, 6}))