# 1. create a map function that return a num + num
# 2. provide a list of number and send it to map function to double every number. 


# 1. create a map function that return a num + num
def add_fun(num):
  return num + num

# 2. provide a list of number and send it to map function to double every number. 
numbers = (1,2,3,4,5)
result = map(add_fun, numbers)

print(list(result))