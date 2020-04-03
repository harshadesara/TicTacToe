def possibilities(value, player):
    if lst2[0] == value and lst2[1] == value and lst2[2] == value:
        a = printouts(player)
    elif lst2[3] == value and lst2[4] == value and lst2[5] == value:
        a = printouts(player)
    elif lst2[6] == value and lst2[7] == value and lst2[8] == value:
        a = printouts(player)
    elif lst2[0] == value and lst2[3] == value and lst2[6] == value:
        a = printouts(player)
    elif lst2[1] == value and lst2[4] == value and lst2[7] == value:
        a = printouts(player)
    elif lst2[2] == value and lst2[5] == value and lst2[8] == value:
        a = printouts(player)
    elif lst2[0] == value and lst2[4] == value and lst2[8] == value:
        a = printouts(player)
    elif lst2[2] == value and lst2[4] == value and lst2[6] == value:
        a = printouts(player)
    else:
        a = 0
    return a


def printouts(player):
    print(player + " won!!!")
    if p1 != player:
        print(p1 + " lost!!!")
    elif p2 != player:
        print(p2 + " lost!!!")
    return 1


def printouts2():
    print(str(lst2[0]) + "  |  " + str(lst2[1]) + "  |  " + str(lst2[2]))
    print("-------------")
    print(str(lst2[3]) + "  |  " + str(lst2[4]) + "  |  " + str(lst2[5]))
    print("-------------")
    print(str(lst2[6]) + "  |  " + str(lst2[7]) + "  |  " + str(lst2[8]))


def player(val, plyr):
    while True:
        no1 = int(input(str(plyr) + "-->Where do you want to place your mark:"))
        if no1 == 9:
            print("Invalid position. Try again!!!")
        elif lst2[no1] == "X" or lst2[no1] == "O":
            print("Invalid position. Try again!!!")
        else:
            break
    for i in range(len(lst2)):
        if no1 == lst2[i]:
            lst2[i] = str(val)
            break
    printouts2()
    a = possibilities(str(val), str(plyr))
    return a


while True:
    print("!!!TIC-TAC-TOE!!!")
    p1 = input("Player1(Mark:X)-->Enter your name:")
    p2 = input("Player2(Mark:O)-->Enter your name:")
    lst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    printouts2()
    i = 0
    while i < 9:
        a = player("X", p1)
        if a == 1:
            break
        i += 1
        if i == 9:
            continue
        b = player("O", p2)
        if b == 1:
            break
        i += 1
    else:
        print("It's a draw!!!")
    data = input("Do you want to play again(Y/N):")
    if data.lower() == "n" or data.lower() == "no":
        print("Thank you for playing!!!")
        break
    elif data.lower() == "y" or data.lower() == "yes":
        continue
    else:
        print("Invalid Option Entered. Exiting!!!")
        break
