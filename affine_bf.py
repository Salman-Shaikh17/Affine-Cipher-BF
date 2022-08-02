#Implemented an affine cipher brute force runner.
affText = input("Enter an affine cypher encrypted text: ")
minusB = 0
inverseA = 0
affText = [(ord(letter) - ord('a')) for letter in affText.lower() \
           if letter.isalpha()]
while inverseA < 26:
    print("\nThe current a^-1 is {} \n\n▼▼▼▼▼▼▼\n".format(inverseA))
    while minusB < 26:
        print("-b is {}".format(minusB))
        print(''.join([chr(ord('a')+code) for code in \
                       [((x+minusB)*inverseA)%26 for x in affText]]))
        minusB+=1
    inverseA+=1
    minusB = 0
