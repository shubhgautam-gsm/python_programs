list1 = [1, 2, 3, 4, 5]
flag = 0

for i in list1:
    print("Current element:", i, end=" ")
    if i == 3:
        print("\nWe are inside pass block")
        flag = 1
    if flag == 1:
        print("\nCame out of pass")
        flag = 0

