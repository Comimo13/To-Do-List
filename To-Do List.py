list = []
while True:
    act = input("What do you want to do?\n1.Add\n2.Delete\n3.Watch\n1 or 2 or 3?:")
    if act == "1":
        list.append(input("What do you want to do?:"))
    if act == "2":
        print(list)
        list.pop(int(input()))
    if act == "3":
        print(list)