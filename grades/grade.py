raw_score = input("Enter a score: ")

try:
    score = float(raw_score)
except:
    score = -1

if score < 0:
    print("Program only accepts numbers (between 0.0 and 1.0)")

if score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
elif score < 0.6 and score >= 0:
    print("F")
