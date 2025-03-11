def Ninety_Nine_Bottles():
    for i in range(99, 0, -1):
        if i == 1:
            print(f"\n{i} bottle of beer on the wall, \n{i} bottle of beer. \nTake one down, pass it around, \n{i-1} bottles of beer on the wall.")
        else:
            print(f"\n{i} bottles of beer on the wall, \n{i} bottles of beer. \nTake one down, pass it around, \n{i-1} bottles of beer on the wall.")
    
Ninety_Nine_Bottles()