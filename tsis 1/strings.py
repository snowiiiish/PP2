#examples - python strings
#1
print("Hello")
print('Hello')
#2
a = "Hello"
print(a)
#3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#4
a = "Hello, World!"
print(a[1])
#5
for x in "banana":
  print(x)
#6
a = "Hello, World!"
print(len(a))
#7
txt = "The best things in life are free!"
print("free" in txt)
#8
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#9
txt = "The best things in life are free!"
print("expensive" not in txt)
#10
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#examples - slicing strings
#1
b = "Hello, World!"
print(b[2:5])
#2
b = "Hello, World!"
print(b[:5])
#3
b = "Hello, World!"
print(b[2:])
#4
b = "Hello, World!"
print(b[-5:-2])

#examples - modify strings
#1
a = "Hello, World!"
print(a.upper())
#2
a = "Hello, World!"
print(a.lower())
#3
a = " Hello, World! "
print(a.strip())
#4
a = "Hello, World!"
print(a.replace("H", "J"))
#5
a = "Hello, World!"
print(a.split(","))
#6



#examples - string concatenation
#1
a = "Hello"
b = "World"
c = a + b
print(c)
#2
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#3


#examples - format strings
#1
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



#examples - escape characters
#1
txt = "We are the so-called \"Vikings\" from the north."



#exercises
#1
x = "Hello World"
print(len(x))
#2
txt = "Hello World"
x = txt[0]
#3
txt = "Hello World"
x = txt[2:5]
#4
txt = " Hello World"
x = txt.strip()
#5
txt = "Hello World"
txt = txt.upper()
#6
txt = "Hello World"
txt = txt.lower()
#7
txt = "Hello World"
txt = txt.replace("H", "J")
#8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))