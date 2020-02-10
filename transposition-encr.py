import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main() :
    keys = open(sys.argv[2], "r").read().split(" ")
    k1 = keys[0]
    k1 = removeDuplicates(k1)
    k1 = k1[:10]
    
    k2 = keys[1]
    k2 = removeDuplicates(k2)
    k2 = k2[:10]
    if len(k1) < 10 or len(k2) < 10 :
        print("ERROR: Please give a nonrepeating 10-character long string for each key.")
        exit(1)
    
    plaintext = open(sys.argv[1], "r").read()
    #plaintext = toLetters(plaintext)
    plaintext = addTrailingX(plaintext)
    
    print("Encrypting...")
    ciphertext = encrypt(plaintext, k1)
    ciphertext = encrypt(ciphertext, k2)
    print("Done")
    
    writeCipherTextToFile(ciphertext)

def removeDuplicates(key) :
    for i in range(len(key)) :
        for j in range(i+1, len(key)) :
            if key[i].upper() == key[j].upper() :
                key = key[:j].upper() + key[j+1:].upper()
                key = removeDuplicates(key)
                return key
    return key

def encrypt(plaintext, key) :
    
    ciphertext = ""
    columns = []
    
    for i in alphabet :
        for j in range(len(key)) :
            if i.upper() == key[j].upper() :
                columns.append(j)
    
    for col in columns :
        for i in range(col, len(plaintext), 10) :
            ciphertext += plaintext[i]
    
    return ciphertext

def toLetters(text) :
    return ''.join(filter(str.isalpha, text)).upper()

def addTrailingX(text) :
    while len(text) % 10 != 0 :
        text += 'X'
    return text

def writeCipherTextToFile(ciphertext) :
    file = open(sys.argv[1].replace(".txt", ".cipher"), "w")
    file.write(ciphertext)
    file.close()

if __name__ == '__main__' :
    main()
