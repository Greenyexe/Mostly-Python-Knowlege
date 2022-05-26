# str.format() = optional method that gives users more control when displaying output

#animal = 'cow'
#item = 'moon'

#print('The ' + animal + ' jumped over the ' + item)
#print('The {} jumped over the {}'.format(animal, item)) # in order
#print('The {1} jumped over the {0}'.format(item, animal)) # positional argument
#print('The {animal} jumped over the {item}'.format(animal = 'cow', item = 'moon')) # keyword argument. You can re-use the keyword pairs in the statement

#text = "The {} jumped over the {}"
#print(text.format(animal, item))




#name = 'Bruno'

#print('Hello my name is {}'.format(name))
#print('Hello my name is {:10}. Nice to meet you'.format(name))
#print('Hello my name is {:<10}. Nice to meet you'.format(name))
#print('Hello my name is {:>10}. Nice to meet you'.format(name))
#print('Hello my name is {:^10}. Nice to meet you'.format(name))




number = 3.14159
number2 = 1000

print('The number pi is {:.2f}'.format(number)) # f means floating point method and will round
print('The number is {:,}'.format(number2)) # adds commer 
print('The number is {:b}'.format(number2)) # display as binary
print('The number is {:o}'.format(number2)) #octal
print('The number is {:X}'.format(number2)) # hexa dec
print('The number is {:E}'.format(number2)) #scientific notation