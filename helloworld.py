import random

def main():
	name = 'Adam'

	rand_a = random.randint(0, 100)
	rand_b = random.randint(0, 100)

	sm = rand_a + rand_b
	av = float(rand_a + rand_b) / 2.0
	
	print(name)
	print(rand_a)
	print(rand_b)
	print('Sum = ' + str(sm))
	print('Average = ' + str(av))

if __name__ == '__main__':
	main()
