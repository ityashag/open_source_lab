a=[] 
n=int(input("Number of elements in array:")) 
for i in range(0,n): 
    l=int(input()) 
    a.append(l) 
print("original array : ",a)

for i in range(0,n):
    for j in range(i,n):
        if(a[i]>a[j]):
            a[i]=a[i]+a[j] 
            a[j]=a[i]-a[j] 
            a[i]=a[i]-a[j]
print("sorted array (using selection sort) : ",a)

for i in range(n):
    for j in range(0,n-i-1):
        if(a[j]<a[j+1]):
            a[j+1]=a[j+1]+a[j] 
            a[j]=a[j+1]-a[j] 
            a[j+1]=a[j+1]-a[j]
  
print("sorted array in non-increasing form (using bubble sort) : ",a)       

for i in range(1,n):
    k = i
    key = a[k]
    n = i-1
    while(n>-1):
        if(a[n]>key):
            a[n+1]=a[n]
            n-=1
        else:
            break
    a[n+1]=key
print("sorted array (using insertion sort) : ",a) 
