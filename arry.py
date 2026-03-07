from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(len(arr))

arr=array('i',[10,20,30])
arr.append(40)
print(arr)

 
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)


arr=array('i',[10,20,30,40])
arr.remove(20)
print(arr)


arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(array)


arr=array('i',[10,20,30,40])
print(arr.index(30))


arr=array('i',[10,20,30,40])
print(arr.count(20))


arr=array('i',[10,20,30,40])
arr.reverse()
print(arr)