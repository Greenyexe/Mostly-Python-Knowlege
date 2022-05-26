#slicing = create a substring by extracting elements from another string
#indexing[] or slice()
#[start:stop:step]
name = "Bruno Greenfield"
website = "http://apple.com"
website2 = "http://google.com"

firstName = name[0:5]  #no need to write the zero as python just assumes its nothing if you put nothing
lastName = name[6:16] #no need to write the end number as python just assumes if you put nothing you want to go to the end
funkyName = name[0:16:2]  #don't have to write the 0 and 16, just use collons as python assumes the values as mentioned above
reversedName = name[::-1]  #-1 to count backwards as the step
websiteSlice = slice(7, -4) #-4 counts backwards from the end number. Remeber end is exclusive!

print(firstName)
print(lastName)
print(funkyName)
print(reversedName)

print(website[websiteSlice])
print(website2[websiteSlice])