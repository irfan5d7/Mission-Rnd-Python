__author__ = 'Kalyan'


def get_hcf(first, second):
    result = []
    for x in first:
        for y in second:
            if x[0] == y[0]:
                if x[1] <= y[1]: result.append(x)
                else: result.append(y)
    return result


def get_lcm(first, second):
    result = []
    if len(first) == 0:
        return second
    if len(second) == 0:
        return first
    first = first + list(set(second) - set(first))
    flag = 0
    while (len(first) != 0):
        flag = 0
        for x in first:
            for y in first:
                if x[0] == y[0] and (x != y):
                    if x[1] > y[1]:
                        result.append(x)
                        first.remove(y)
                        first.remove(x)
                        flag = 1
                        break
                    elif x[1] < y[1] and y not in result:
                        result.append(y)
                        first.remove(x)
                        first.remove(y)
                        flag = 1
                        break
            if flag == 0:
                result.append(x)
                first.remove(x)
                break
    result.sort()
    return result


def multiply(first, second):
    result = []
    temp=[]
    if len(first) == 0: return second
    if len(second) == 0: return first
    first= first + second
    z = tuple([0, 0])
    j=0
    while j<len(first):
        x=list(first[0])
        i=1
        if x==[0,0]:
            first.remove(first[0])
        else:
            while i<len(first):
                y=list(first[i])
                if x[0] == y[0]:
                    x[1] = x[1]+y[1]
                    first[i]=z
                i+=1
            result.append(tuple(x))
            first.remove(first[0])
    j+=1
    result.sort()
    return result