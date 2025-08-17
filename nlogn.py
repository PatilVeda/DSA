# n =1000
# inti,j,k= 0
# # 2,4,8(10)
# # 2,4,8,16,32,64(100)
# # 2,4,8,16,32,64,128,256,512(1000)

# for(i=n/2;i<=n;i++)  {
#     for(j=2;j<=n;j=j*2){
#         k=k=n/2
#     }
# }

# O(n/2)*O(logn) = o(n/2 * logn)
                # =0(1/2 nlogn)
                # = o(nlogn)






L = [1,2,3,4,5]
for i in range(0,len(L)):
    for j in range(i+1,len(L)):
        print('{},{})'.format(L[i],L[j]))


# O(n)*O(n-1)
# O(n^2-n)
# O(n^2)
