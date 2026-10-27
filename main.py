

def avg():
  a = int(input("Enter first value:"))
  b = int(input("Enter first value:"))
  c = int(input("Enter first value:"))

  average = (a+b+c)/3
  # print(average)
  return average


# avg()

def calc_matrix(average):
  return average*average*average
  # print("weight average is ", average)

a = calc_matrix(avg())

print(a)