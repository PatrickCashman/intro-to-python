weight = input("weight: ")
user_weight = input("(k)g or (L)bs: ").upper()

if (user_weight == "L"):
    new_weight = (float(weight) * 0.45)
    print("Weight in Kg: " + str(new_weight))
if(user_weight == "K"):
    new_weight = (float(weight) / 0.45)
    print("Weight in Lbs: " + str(new_weight))