# nested functions calls = function calls inside other function calls
# innermost function calls are resolved first 
# returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
#num = float(num) float converts into float
#num = abs(num) abs converts into the absolute value
#num = round(num) rounds it to the nearest whole number
#print(num) 

print(round(abs(float(input("Enter a whole positive number: "))))) #shorter way of writing what it above using nested funtion calls