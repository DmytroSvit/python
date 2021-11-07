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

while True:
    try:
        n=int(input('Enter size of array: '))
        if n > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('You must enter positive integer number as a size of array')
    
array = []
print(f'Enter {n} integer elements of array: ')

for i in range(n):
    while True:
        try:
            array.append(int(input()))
            break
        except ValueError:
           print('You must enter integer number as a element of array') 
  
print('Product of numbers to the last positive number in array: ', product(array))

