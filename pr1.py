def product(array):
    lastPositive = -1
    for i in range(len(array)):
        if array[i] > 0:
            lastPositive = i
    if lastPositive >= 0:
        product = 1
        for i in range(lastPositive+1):
            product *= array[i]
        return product
    else:
        return 'There is no positive integer in array.'

n=5
array = []

for i in range(n):
    array.append(int(input()))
  
print('Product of numbers to the last positive number in array: ', product(array))

      
