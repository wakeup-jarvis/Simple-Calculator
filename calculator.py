def calculator(a,b,operator):
    if operator=="-":
        return a-b
    elif operator=="+":
        return a+b
    elif operator=="*":
        return a*b
    elif operator=="/":
        return a/b
    else:
        return "Invalid Input"
cal = calculator(5,8,"a")
print(cal)
print("Done")
