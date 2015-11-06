#Get decimal number from the user
d = int(input("Please input a decimal number: "))

#Create an empty strimg
s = str("")

while d >= 1:
	#Find the remainder when d is devided by 2
	rem = (d % 2)
	#Convert rem to int
	rem = int(rem)
	#Divide the binary number by 2
	ans = (d / 2)
	#Update d to the divided number
	d = ans
	#Add rem to the end of the string
	s = (s + str(rem))

#Print the string
print (s[::-1])