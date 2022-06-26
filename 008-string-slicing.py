import string

# slicing - create a substring by extracting elements from another
# string
#       indexing[] or slice()
#       [start:stop:step]

name = "Bro Code"

firstName = name[0:3]   #[0:3]
firstName1 = name[:3]   #[start:3]
lastName = name[4:]     #[4:end]

print(firstName)
print(firstName1)
print(lastName)

funkyName = name[0:8:2]

print(funkyName)

funkyName1 = name[::3]

print(funkyName1)

reversedName = name[::-1]
print(reversedName)

website1 = "https://yahoo.com"
website2 = "https://wikipedia.com"

slice1 = slice(8, -4)
print(website1[slice1])
print(website2[slice1])