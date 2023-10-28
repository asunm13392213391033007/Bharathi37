def leapyear(year):
  if (year % 4 == 0 and year % 100 != 0):
    return True
  elif (year % 400 == 0):
    return True
  else:
    return False


year = int(input("enter year:"))
if leapyear(year):
  print(year, "leap year")
else:
  print(year, "is not leap year")
