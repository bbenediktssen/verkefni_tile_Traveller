#Notast við x & y ás, og plúsa alltaf við x eða y ásinn eftir áttum. Finna út hvar manneskjan er í hverju sinni og skrifa inn hvaða áttir hún getur farið í
'''
Leikurinn virkar eins og völundarhús. Leikmaður byrjar í reit 1,1 og á að komast á reit 3,1 með því að fara "North, south, east, west" eftir
upplýsingum sem eru gefnar upp á skjánum. Þegar leikmaður hefur komist á reit 3,1 fær hann skilaboð um að hann hefur unnið leikinn.
https://github.com/bbenediktssen/verkefni_tile_Traveller/blob/master/tileTraveller.py
'''

x = 1
y = 1
a = True
b = True
while a == True:
    if (x == 1 and y == 1) or (x == 2 and y == 1) or (x == 3 and y == 1):
        if ((x == 3) and (y == 1)):
            print("Victory!")
            a = False
        else:
            if b == True:
                print("You can travel: (N)orth.")
            direction = str(input("Direction: "))
            b = True
            if ((direction == "n") or (direction == "N")):
                y += 1
            else:
                print("Not a valid direction!")
                b = False
    elif x == 1 and y == 2:
        if b == True:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = str(input("Direction: "))
        b = True

        if ((direction == "e") or (direction == "E")):
            x += 1
        elif ((direction == "n") or (direction == "N")):
            y += 1
        elif ((direction == "s") or (direction == "S")):
            y -= 1
        else:
            print("Not a valid direction!")
            b = False

    elif x == 1 and y == 3:
        if b == True:
            print("You can travel: (E)ast or (S)outh.")
        direction = str(input("Direction: "))
        b = True
        if ((direction == "e") or (direction == "E")):
            x += 1
        
        elif ((direction == "s") or (direction == "S")):
            y -= 1
        else:
            print("Not a valid direction!")
            b = False

    elif (x == 2 and y == 2) or (x == 3 and y == 3):
        if b == True:
            print("You can travel: (S)outh or (W)est.")
        direction = str(input("Direction: "))
        b = True
        if ((direction == "w") or (direction == "W")):
            x -= 1
        elif ((direction == "s") or (direction == "S")):
            y -= 1
        else:
            print("Not a valid direction!")
            b = False
    
    elif x == 2 and y == 3:
        if b == True:
            print("You can travel: (E)ast or (W)est.")
        direction = str(input("Direction: "))
        b = True
        if ((direction == "e") or (direction == "E")):
            x += 1
        elif ((direction == "w") or (direction == "W")):
            x -= 1
        else:
            print("Not a valid direction!")
            b = False
    
    elif x == 3 and y == 2:
        if b == True:
            print("You can travel: (N)orth or (S)outh.")
        direction = str(input("Direction: "))
        b = True
        if ((direction == "n") or (direction == "N")):
            y += 1
        elif ((direction == "s") or (direction == "S")):
            y -= 1
        else:
            print("Not a valid direction!")
            b = False
    
    

