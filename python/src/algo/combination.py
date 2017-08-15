def combination(elems, result_set):
    if len(elems) < 1:
        return
    if len(elems) == 1:
        result_set.add((elems.pop(0),))
    else:
        e = elems.pop()
        combination(elems, result_set)
        newset = set()
        for t in result_set:
            newset.add( t + (e,) )
        result_set |= newset
        result_set.add( (e,) )

if __name__ == "__main__":
    elems = [1, 2, 3, 4]
    myresult = set()
    combination(elems, myresult)
    print(myresult)