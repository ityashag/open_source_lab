#include <stdio.h>

int binary_search(int arr[],int key,int n)
{
    int s = 0;
    int e = n-1;
    
    while(s<=e)
    {
        int mid = s+(e-s)/2;
        
        if(arr[mid]==key)
        {
            return mid;
        }
        else if(arr[mid]<key)
        {
            s=mid+1;
        }
        else
        {
            e=mid-1;
        }
        
    }
    return -1;
    
}
int main()
{
    int t;
    printf("Enter the number of test cases : ");
    scanf("%d",&t);
    while(t--)
    {
        int n;
        printf("Enter the length of array : ");
        scanf("%d",&n);
        int arr[n];
        
        printf("Ener the array elements : ");
        for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }
        
        printf("Enter the key : ");
        int key;
        scanf("%d",&key);
        int bin_search =  binary_search(arr,key,n);
        printf("Element present at index : %d \n \n",bin_search);
    }
    
}
