scope = int(input('Enter Score: '))
if scope >= 90:
    print("A")
elif scope < 90 and scope >= 80:
    print("B")
elif scope < 80 and scope >= 70:
    print("C")
elif scope < 70 and scope >= 60:
    print("D")
else:
    print("F")
