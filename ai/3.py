# *_*coding:utf-8 *_*
def binaery_search(list,item):
    low=0
    high=len(list)-1

    while low <= high:
        mid=int((low+high)/2)
        guess=list[mid]
        if guess == item:
            return mid
        if guess >item:
            high=mid-1
        else:
            low=mid+1
    return None


my_list=[1,3,5,7,9,11]

print(binaery_search(my_list,1))
print(binaery_search(my_list,3))
print(binaery_search(my_list,5))
print(binaery_search(my_list,7))
print(binaery_search(my_list,9))
print(binaery_search(my_list,11))
print(binaery_search(my_list,-1))

