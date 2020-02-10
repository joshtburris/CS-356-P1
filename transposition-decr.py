import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

def main() :
    keys = open(sys.argv[2], "r").read().split(" ")
    k1 = keys[0]
    k2 = keys[1]
    
    ciphertext = open(sys.argv[1], "r").read()
    
    print("Decrypting...")
    plaintext = decrypt(ciphertext, k2)
    plaintext = decrypt(plaintext, k1)
    print("Done")
    plaintext = removeTrailingX(plaintext)
        
    writePlainText(plaintext)


def decrypt(text, key) :
    
    
    plaintext = ""
    for i in range(len(text)) :
        plaintext += " "
    
    columns = []
    for i in alphabet :
        for j in range(len(key)) :
            if i.upper() == key[j].upper() :
                columns.append(j)
    
    collen = len(text) / 10
    
    index = 0
    for col in columns :
        for i in range(col, len(text), 10) :
            plaintext = plaintext[:i] + text[index] + plaintext[i+1:]
            index += 1
    
    
    return plaintext

def writePlainText(text) :
    file = open(sys.argv[1].replace(".cipher", ".txt"), "w")
    file.write(text)
    file.close()

def removeTrailingX(plaintext) :
    while plaintext[-1] == "X" :
        plaintext = plaintext[:len(plaintext)-1]
    return plaintext

if __name__ == '__main__' :
    main()
