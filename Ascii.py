import collections

reg = input("What's your regular email address?: ")
que = input("What is the email address in question?: ")

reg_ascii = []
for character in reg:
	reg_ascii.append(ord(character))
print(reg_ascii)

que_ascii = []
for character in que:
	que_ascii.append(ord(character))
print(que_ascii)

if collections.Counter(reg_ascii)==collections.Counter(que_ascii):
	print("Not fishy")
else:
	print("Something is fishy")




#     python3 desktop/ascii.py