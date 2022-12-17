import os

clear = lambda: os.system('cls')

def Settings(mods, ChosenMod):
    """ Меню параметров, позволяет менять мод, более не для чего пока не используется

    :param mods:
    :param ChosenMod:
    :return:
    """
    #   Menu for settings
    buffer = 1337
    while buffer != "0":
        print("\tSETTINGS\n\t1) Choose mod\n\t2) Load language(WORK IN PROGRESS)\n\t0) Back\n\tInput > ", end="")
        buffer = input()
        if buffer == "1":
            buffer = 1
            clear()
            for i in mods:
                print("\t" + str(buffer) + ")", i)
                buffer += 1
            print("\tInput > ", end="")
            ChosenMod = mods[int(input()) - 1]
        elif buffer == "2":
            for i in mods:
                print("aboba")
        clear()
    return mods, ChosenMod