import os

def Settings(mods, ChosenMod):
    clear = lambda: os.system('cls')

    #   Menu for settings

    buffer = 1337
    while buffer != "0":
        print("\tSETTINGS\n\t1) Choose mod\n\t2) Save settings\n\t0) Back\n\tInput > ", end="")
        buffer = input()
        if buffer == "1":
            buffer = 1
            for i in mods:
                print(buffer, ". ", i)
                buffer += 1
            print("\tInput > ", end="")
            ChosenMod = mods[int(input()) - 1]
        clear()
    return mods, ChosenMod