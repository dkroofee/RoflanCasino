word1 = set()
word2 = set()
street1 = input()
while street1 != '':
    word1.add(street1)
    street1 = input()
street2 = input()
while street2 != '':
    word2.add(street2)
    street2 = input()
intersection = word1 & word2
if intersection == set():
    print('EEMPTY')
else:
    for i in intersection:
        print(i)
    print('\n')