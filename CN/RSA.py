import math
from time import sleep


def if_prime(x):  # prime number checker
    if x == 2:  # base case 2
        return True
    elif x < 2 or x % 2 == 0:  # checking if even
        return False
    else:
        for y in range(2, x):
            if not x % y:  # checking if divisible by nums other than 1 and itself
                return False
    return True


def egcd(e, r):  # GCD
    while r != 0:
        e, r = r, e % r
    return e


def eugcd(e, r):
    for x in range(1, r):
        while e != 0:
            a, b = r // e, r % e
            if b != 0:
                print(f'{r} = a * ({e}) + {b}')
            r, e = e, b


def eea(a, b):
    if a % b == 0:
        return (b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s - ((a // b) * t)
        print(f'{gcd}={a} * ({t}) + ({s}) * ({b})')
        return (gcd, t, s)


def mult_inv(e, r):
    gcd, s, _ = eea(e, r)
    if gcd != 1:
        return None
    else:
        if s < 0:
            print(f's={s}. Since {s} is less than 0, s=s(modr), i.e., s={s%r}')
        elif s > 0:
            print(f's={s}')
        return s % r


def encrypt(pub_key, n_text):  # Encryption
    e, n = pub_key
    x = []
    m = 0
    for i in n_text:
        if(i.isupper()):
            m = ord(i) - 65
            c = (m**e) % n
            x.append(c)
        elif(i.islower()):
            m = ord(i) - 97
            c = (m**e) % n
            x.append(c)
        elif(i.isspace()):
            spc = 400
            x.append(400)
    return x


def decrypt(priv_key, c_text):  # Decryption
    d, n = priv_key
    txt = c_text.split(',')
    x = ''
    m = 0
    for i in txt:
        if i == '400':
            x += ' '
        else:
            m = (int(i)**d) % n
            m += 65
            c = chr(m)
            x += c
    return x


print('Welcome to the RSA Encrypter/Decrypter')
print('***************************************')
sleep(1)

while True:
    # prime int input
    print("Enter <p> and <q> values:")
    p = int(input('Enter prime number p: '))
    q = int(input('Enter prime number q: '))
    print('***************************************')
    if (if_prime(p) == False) | (if_prime(q) == False):
        continue
    else:
        break

n = p * q  # RSA Modulation
print(f'RSA Modulus: {n}')

r = (p - 1) * (q - 1)  # Eulers Toitent
print(f'Eulers Toitent: {r}')
print('***************************************')
sleep(1)
# e calculation
for i in range(1, 1000):
    if (egcd(i, r) == 1):
        e = i
print(f'The value for e is {e}')
print('***************************************')
sleep(1)

# calculating d public and private key
print("Euclid's Algorithm:")
eugcd(e, r)
print("End of the steps used to achieve Euclid's algorithm.")
print('***************************************')
sleep(1)

print("Euclid's extended algorithm:")
d = mult_inv(e, r)
print("End of the steps used to achieve the value of 'd'.")
print(f'The value of d is: {d}')
print('***************************************')
sleep(1)

public = (e, n)
private = (d, n)
print(f'Private key is {private}')
print(f'Public key is {public}')
print('***************************************')
sleep(1)

# printing messages
message = input("What to encrypt/decrypt? (Seperate numbers with ',' for decryption): ")
print(f'Your message is: {message}')
sleep(1)
print('***************************************')
# choosing ecnrypt of decrypt and printing respectively
choose = input("Type '1' for encryption and '2' for decryption: ")
print('***************************************')
sleep(1)

if choose == '1':
    enc_msg = encrypt(public, message)
    print(f"Your encrypted message is {enc_msg}")
    sleep(1)
    print("Thank you for using the program, goodbye!")
elif choose == '2':
    print(f"Your decrypted message is: {decrypt(private, message)}")
    sleep(1)
    print("Thank you for using the program, goodbye!")
else:
    print("You entered the wrong option.")
    sleep(1)
    print("Thank you for using the program, goodbye!")
