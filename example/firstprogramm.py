# Dieses Programm sagt "Hallo" und fragt nach Ihrem Namen.


def printPicnic(itemsDict,leftWidth,rightWidth):
    print('Picnic Items'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

PicnicItems ={'Sandwiches': 4,'apples': 12,'cups': 4,'cookies': 8000}

printPicnic(PicnicItems, 12 ,5)
printPicnic(PicnicItems, 20 ,6)
