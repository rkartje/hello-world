#make an empty dictionary
d = {}
l = []
#assign value 5 to key 3
#a key can be an integer or a string at least
d[3] = 5
l.append(2)
l.append(3)
#retrieve and print element or value at key 3
print(d[3])
print(l[0], l[1])

#construct a dictionary that already has some items in it
dog_breeds = {"Jeanie":"Border Terrier", "Ernie":"Rod Ridgeback", "Romeo":"Shitzu"}
for name in dog_breeds:
    print(dog_breeds[name])
    #now include dot values

for dog_breed in dog_breeds.values():
    print(dog_breed)
    
#print out name and breed
for name, breed in dog_breeds.items():
    print(name, breed)