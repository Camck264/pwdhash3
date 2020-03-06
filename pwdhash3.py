import hashlib

def hashingMethod(passwordHash):
    hash1 = hashlib.md5(passwordHash)
    print ("Your password is: "), hash1.hexdigest()

def main():
    print ("Password hashing script")
    passwordHash = raw_input ("Enter your password: ")
    hashingMethod(passwordHash)

if __name__ == '__main__':
    main()