def computepay(hours, rate):
    if hours > 40:
        return (hours * rate) + ((hours - 40.0) * (rate * 0.5))
    else:
        return hours * rate


hours = input("Enter hours: ")
rate = input("Enter rate: ")

hours = float(hours)
rate = float(rate)

print("Pay ", computepay(hours, rate))
