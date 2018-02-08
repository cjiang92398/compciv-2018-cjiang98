# This function takes a small spin on the FizzBuzz problem, always printing out
# the number in addition to 'FoozBuzz', 'Fooz', 'Buzz', or nothing.
def fob(num):
	for i in range(1, num + 1):
		string = str(i) + ' '
		if i % 3 == 0 and i % 5 == 0: 
			string +='FoozBuzz'
		elif i % 3 == 0:
			string +='Fooz'
		elif i % 5 == 0:
			string +='Buzz'
		print(string)
