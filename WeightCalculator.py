print("Weight Calculator")
weight = float(input("Weight: "))
metrics = input("(K)g or (L)bs: ")

if metrics.upper() == "K":
    calc = 2.2 * weight
    print("Weight in lbs: " + str(calc))
elif metrics.upper() == "L":
    calc = 0.45*weight
    print("Weight in kgs: " + str(calc))
else:
    print("Wrong input!!!")