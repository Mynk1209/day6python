#loops importent
#1.for
#.2.while

# for i in range(10):
#      print("hello world ",i)

# i = 0 
# while(i<=10):
#     print("hello world",i )
#     i +=1

# ls =[23,456,4,85,56,66,654,765,47,693,90,67,63]
# if 68 in ls:
#     print("yes")
# else:
#     print("no")
#     count=0
#     for item in ls:
#         if item == 85:
#             print ("yes",count)
#             count +=1
      
# print("final count",count)
ls=[2,-7,-55,45,32,66,77,4,1,77,9,98]
largest=-float('inf')
smallest=float('inf')
for i in ls:
    if i>largest:
        largest=i
    elif i<smallest:
        smallest=i
print(smallest)
print(largest)
