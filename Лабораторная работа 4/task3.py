def delete(list_, index=-1): # встроенными функциями
    list_.pop(index)
    return list_

def delete2(list_, index=None): # слайсированием
    newlist = []
    for i in range(len(list_)):
        if index==None:
            newlist = list_[:-1]
        else:
            newlist = list_[:index] + list_[index+1:]
    return newlist

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
print('\n')
print(delete2([0, 0, 1, 2], index=0))  # [0, 1]
print(delete2([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete2([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]