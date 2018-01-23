def selection(prime, first): # Only selects the prime numbers from the first to last
    result = []
    for n in prime:
        if int(n) > int(first):
            result.append(n)
    return result

def primarize(first, last):
    nonprime = 0
    prime = [2]
    x = 0

    for num in range(3, int(last) + 1): # Tries every number
       while x < len(prime): # Controls index size
         if num % prime[x] == 0: # Sees if it is prime
           nonprime += 1
           x = 0 # Resets index
           break # Throws the number away
         else:
           x += 1 # Tries another number
       else:
         prime.append(num)
         x = 0

    selected_prime = selection(prime, first)
    prime_dif = len(prime) - len(selected_prime)

    print selected_prime
    print "There are %s prime numbers between %s and %s" % (len(selected_prime), int(first), int(last))
    if prime_dif != 0:
        print "There are %s prime numbers from 0 to %s" % (len(prime), int(last))
        print "%s prime numbers are smaller than %s" % (prime_dif, first)

primarize((raw_input("Compute all prime numbers from ")),(raw_input("To ") ))
