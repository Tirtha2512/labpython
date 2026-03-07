from array import array
arr=array("i",[20,30,40,50])
print(arr)
print(type(arr))
#len()-number of elements
from array import array
arr=array("i",[10,20,30,40,50])
print(len(arr))
#append(x)-Add element at end
arr=array("i",[10,20,30])
arr.append(40)
print(arr)
#insert(pos,x)-Insert at position
arr=array("i",[10,20,40])
arr.insert(2,30)
print(arr)
#remove(x)-remove first occurrence
arr=array("i",[10,20,30,20,40])
arr.remove(20)
print(arr)
#pop()-remove and return last element
arr=array("i",[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)
#index(x)-find index of element
arr=array("i",[10,20,30,40])
print(arr.index(30))
#count(x)-count occurnences
arr=array("i",[10,20,30,20,40])
print(arr.count(20))
#reverse()-reverse Array
arr=array("i",[10,20,30,40])
arr.reverse()
print(arr)