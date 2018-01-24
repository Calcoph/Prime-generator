def selection(prime, first): # Only selects the prime numbers from the first to last
    result = []
    for n in prime: # Checks every prime
        if int(n) > int(first): # Filters the prime smaller than the first one
            result.append(n)
    return result

def primarize(first, last): # Checks for primes
    nonprime = 0 # !!!Unused!!! Counts the numbers that have been checked and aren't primes
    prime = [2] # Starts the prime list so it can work properly
    x = 0 # Used for iteration over the prime list

    for num in range(3, int(last) + 1): # Tries every number
       while x < len(prime): # Controls index size
         if num % prime[x] == 0: # Sees if it is prime
           nonprime += 1 # !!!Unused!!! Adds to counter
           x = 0 # Resets index
           break # Throws the number away
         else:
           x += 1 # Tries next index
       else: # The number checked is a prime
         prime.append(num) # Adds the number to prime list
         x = 0 # Resets index

    selected_prime = selection(prime, first) # Makes the list the user wanted
    prime_dif = len(prime) - len(selected_prime) # How many primes were lower than the first prime wanted

    return selected_prime, prime, prime_dif

first = raw_input("Compute all prime numbers from ") # Requests the start of the prime list
last = raw_input("To ") # End of the prime list
primes, allprimes, prime_dif = primarize(first, last)
print primes
print "There are %s prime numbers between %s and %s" % (len(primes), int(first), int(last))
if prime_dif != 0:
    print "There are %s prime numbers from 0 to %s" % (len(allprimes), int(last))
    print "there are %s prime numbers smaller than %s" % (prime_dif, first)
