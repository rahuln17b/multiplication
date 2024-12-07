def probaofb(a, b, total):
    proba = orange/total
    probga = blue/(total-1)
    probab = proba*probga
    return round(probab,3)

orange = int(input("Enter orange balls"))
blue = int(input("Enter blue balls"))
total = orange+blue

print('Probability of getting 1st orange and 2nd blue ball: ')
print(probaofb(orange, blue, total))