import random
print('Your lotto numbers are:', random.randint(1, 51), random.randint(1, 51), random.randint(1, 51), random.randint(1, 51), random.randint(1, 51),random.randint(1, 51), '\nGood Luck!')
lotto = random.sample(range(1, 51), 6)
lottoJoin = " ".join(str(num) for num in lotto)
print("Here are your lotto numbers: " + lottoJoin,"\nGood Luck!")
