def findLargerNum (x, y):
    if x > y:
        print (f"{x} is larger than {y}")
        return x
    elif x < y:
        print (f"{y} is larger than {x}")
        return y
    else:
        print ("both numbers are equal")
    return None