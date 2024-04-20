corna = 10
cornb = 20
side = 3

for i in range(1,101):
    for j in range(1,101):
        x = corna + (i * side/100)
        y = corna + (j * side/100)
        c = int(x**2 + y**2)
        if c % 2 == 0:
            print("black")
            print(f"x = {i}, y = {j}")
        elif c % 3 == 0:
            print("blue")
            print(f"x = {i}, y = {j}")
