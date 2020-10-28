raw_hours = input('Enter hours: ')
raw_rate = input('Enter rate: ')

hours = float(raw_hours)
rate = float(raw_rate)

if hours > 40:
  regular_pay = hours * rate
  extra_time = (hours - 40.0) * (rate * 0.5)
  overtime_pay = regular_pay + extra_time
  print(overtime_pay)
else:
  regular_pay = hours * rate
  print(regular_pay)
