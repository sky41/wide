arr1 =[1,3,4,6,10,12]#初始化两个数组
arr2 =[2,5,8,11,]
ind = 0
ans = arr1.copy()#ans初始化为arr1
for i in range(0,len(arr2)):
    while ind < len(arr1):#ind的范围不能超过数组元素下标的最大值
        if arr2[i] <= arr1[ind]:
            ans.insert(ind + i,arr2[i])
            break
        else:
            ind += 1
    else:
        ans = ans + arr2[i:]
#arr1 =[1,3,4,6,10,12]#初始化两个数组
#arr2 =[2,5,8,11,]
#ind = 0
#ans = arr1.copy()#ans初始化为arr1
#for i in range(0,len(arr2)):
#    while ind < len(arr1):#ind的范围不能超过数组元素下标的最大值
#        if arr2[i] <= arr1[ind]:
#            ans.insert(ind + i,arr2[i])
#            break
#        else:
#            ind += 1
#    else:
#        ans = ans + arr2[i:]
#