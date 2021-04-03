
n_terms = int(input('How many terms? '))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
    print("please enter a positive integer")

elif n_terms == 1:
    print("Fibonacci sequence upto", n_terms, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1
