""" Build function to find the prime factors of any given number. """

def get_prime_factors(N):
	""" Initializing an empty list variable. """
	factors = list()
	""" Define first number to use as divisor. """
	divisor = 2
	""" Iterate until we get to 1. """
	while (divisor <= N):
		""" Check the result of division done without reminder. """
		if (N % divisor) == 0:
			factors.append(divisor)
			N = N / divisor
		else:
			""" Increment divisor if the number become odd. """
			divisor += 1
	return factors

# Another option
# def prime_factor(N, f):
# 	if N < f:
# 		return []
# 	elif N % f == 0:
# 		return [f] + prime_factor(N / f, 2)
# 	return prime_factor(N, f+1)
