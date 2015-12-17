# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

total = 0
start = 1
stop  = 2000000


def check_if_prime(num):
	if num<2:
		return False
	if num==2:
		return True
	if not num&1:
		return False
	for x in range(3, int(num**0.5)+1, 2):
		if num % x == 0:
			return False
	print "found one", num
	return True

for i in range(start,stop):
	if check_if_prime(i):
		total += i
		print total

print total