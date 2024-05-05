#Grokking algorithms

#4.1

#def my_sum(ml):
#    if ml == []:
#        return 0
#    return ml[0] + my_sum(ml[1:])
#ml = [2,4,6]
#print(my_sum(ml))

#4.2

#def my_sum(ml):
#    if ml == []:
#        return 0
#    return 1 + my_sum(ml[1:])
#
#ml = [1,5,7,9,3,6,7,5]
#print(my_sum(ml))

#4.3

#def my_max(ml):
#    if len(ml) == 1:
#        return ml[0]
#    else:
#        find = my_max(ml[1:])
#        if ml[0] > find:
#            return ml[0]
#        else:
#            return find
#        
#ml = [1,6,77,0,2,4,5,7,9]
#print(my_max(ml))

#4.4

#def binary(ml,target):
#    if ml == []:
#        return False
#    
#    mid = len(ml) // 2
#    if ml[mid] == target:
#        return True
#    elif ml[mid] > target:
#        return binary(ml[:mid], target)
#    else:
#        return binary(ml[mid+1:], target)
#
#target = int(input("Enter a nummber to search: "))
#ml = [1,2,4,5,6,7,8,9,11]
#print(binary(ml,target))

#quick sort

#def qsort(ml):
#    if len(ml) < 2:
#        return ml
#    else:
#        pivot = ml[0]
#        less = [i for i in ml[1:] if i <= pivot]
#        grater = [i for i in ml[1:] if i > pivot]
#        return qsort(less) + [pivot] + qsort(grater)
#
#ml = [10,8,3,9,0,1,3,4,5]
#print(qsort(ml))


