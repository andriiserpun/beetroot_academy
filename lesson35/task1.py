import concurrent.futures
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
        for number, result in zip(numbers, results):
            if result:
                primes.append(number)
    return primes

def filter_primes_process(numbers):
    primes = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(is_prime, numbers)
        for number, result in zip(numbers, results):
            if result:
                primes.append(number)
    return primes

# Test the functions
NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

primes_thread = filter_primes(NUMBERS)
print("Primes using ThreadPoolExecutor:", primes_thread)

primes_process = filter_primes_process(NUMBERS)
print("Primes using ProcessPoolExecutor:", primes_process)
