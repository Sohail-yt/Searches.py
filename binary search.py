def binary(a,f,strt,end):
    mid=a[0]+a[-1]//2
#     mid = l + (r - l) // 2
    if mid==f:
        return a[mid]
    else:
        if f<a[mid]:
            return binary(a,f,a[0],a[mid-1])
           
           
        else:
            return binary(a,f,a[mid+1],a[-1])
   
a=[5,1,2,5,8,3,0]
f=8
binary(a,f,a[0],a[-1])