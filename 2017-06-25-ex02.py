

vowels = 'aeiou'

first_name = input("First name ===> ")
last_name = input("Last name ===> ")

full_name = "{} {}".format(first_name, last_name)
print("Hello {}".format(full_name))

upper_name = ""
for letter in full_name:
    if vowels.find(letter) != -1:
        letter = letter.upper()
    upper_name += letter

print("And with some upper case vowels: {}".format(upper_name))

# תרגיל 1
boylist = ['yaniv','dan','omer']
girllist = ['limor','adi','dana']

boylist.append('ziv')
print(boylist)
girllist.insert(0,'lior')
print(girllist)

bride = girllist.pop(-1)
print(bride)
print(girllist)

groom = boylist.pop(0)
print(groom)
print(boylist)

# boylist.remove('omer')
boylist.remove(boylist[2])
print(boylist)

names = boylist + girllist

print(names)

# תרגיל 2

boy1 = ['yaniv', 41, True]
boy2 = ['dan', 30, False]
boy3 = ['omer', 10, False]

boy1[1] = 42

print (boy1)

allboys = []
allboys.append(boy1)
allboys.append(boy2)
allboys.append(boy3)

print(allboys)

allboys[0][1] = 41
print(allboys)

allboys.pop(0)
print(allboys)
allboys.remove(allboys[1])
print(allboys)


