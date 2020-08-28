

def is_leap(x):
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)


while True:
    print("---------------------\n")
    print("To quit input '0'")
    print("Enter the Year:")
    year = int(input(">>>: "))
    if year == 0:
        print(">>>: Danke, tschüss!~")
        break
    else:
        if is_leap(year):
            print(">>>: %d is a leap year." % year)
        else:
            print(">>>: %d is not a leap year." % year)
