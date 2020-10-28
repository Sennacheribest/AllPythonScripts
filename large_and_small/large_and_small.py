largest = None
smallest = None

while True:
    sval = input("Enter a number: ")

    if sval == "done":
        break

    try:
        num = int(sval)
    except:
        print("Invalid input")
        continue

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

print("Maximum is", largest)
print("Minimum is", smallest)
