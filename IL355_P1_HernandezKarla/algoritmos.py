
def busqueda_lineal(arr,obj):
    for i,v in enumerate(arr):
        if v==obj:return i
    return -1

def busqueda_binaria(arr,obj):
    l,r=0,len(arr)-1
    while l<=r:
        m=(l+r)//2
        if arr[m]==obj:return m
        l,r=(m+1,r)if arr[m]<obj else(l,m-1)
    return -1
