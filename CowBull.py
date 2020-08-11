import random
def check(guess):
	cow = 0
	bull = 0
	overall = []
	guess = [x for x in str(guess)]
	for i,x in enumerate(guess):
		for j,y in enumerate(secret):
			if x == y :
				if i == j:
					cow += 1
				else:
					bull += 1

	[overall.append('Cow') for x in range(1,cow +1)]
	[overall.append('Bull') for x in range(1,bull +1)]
	overall = random.sample(overall,len(overall))
	print('\n',overall)

	if cow == len(secret):
		return True
	else:
		return False

#Main Code Begin
print("Cow and Bull Game\n")

secret = 1234
secret = [x for x in str(secret)]

print('The number has {} numbers! guess them and we will give you \'cow\' or \'bull\' based on your answer!\n'.format(len(secret)))
while True:
	while True:
		try:
			guess = int(input('Enter your guess >'))
			if len(str(guess)) == 4:
				break
			else:
				print("You need 4 digits!\n")
		except:
			print('Enter a valid digit\n')

	if check(guess):
		break
	else:
		print("\nYou need {} cows to win!".format(len(secret)))
		continue

print("You win! the secret number was {}. Congratulations!".format(''.join(secret)))
