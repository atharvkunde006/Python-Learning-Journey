nums=[10,20,4,45,99]
largest=0
second=0
for num in nums:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        second=num
    print("second largest :",second)