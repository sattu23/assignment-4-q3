def square(number):
      return number * number
numbers = [4, 5, 2, 9]
output = map(square, numbers)
print("Square of the numbers are >>>")
print(list(output))