n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print(f"Expected {n} elements, but got {len(arr)}")
else:
    arr = sorted(set(arr))  # remove duplicates and sort

    if len(arr) < 2:
        print("No second largest")
    else:
        print("Second largest:", arr[-2])
