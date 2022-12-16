import os
import Settings
import Exporter

#   Configuration
clear = lambda: os.system('cls')
Login = os.getlogin()   #Имя пользователя Windows
APPDir = os.getcwd()    #Расположение программы
ModsFoldersWithSaves = ["xcom1"]    #Список модулей
DeffaultPath = "C:/Users/" + Login + "/Documents/OpenXcom/"    #Путь до папки с OpenXCOM
DeffaultPathToMod = DeffaultPath + "mods/" + ModsFoldersWithSaves[0]   #Путь до папки с модификациями OpenXCOM
DeffaultMod = ModsFoldersWithSaves[0]    #По умолчанию выбранная модификация
LanguageFiles = []

#   Search for saves
os.chdir(DeffaultPath + "mods")
buffer = os.listdir()
for i in buffer:
    os.chdir(DeffaultPath + "mods/" + i)
    j = open("metadata.yml").readlines()
    id = ''
    check = 0
    for stroka in j:
        if "id:" in stroka:
            id = stroka[4:-1]
        if "isMaster: true" in stroka:
            check = 1
    if check:
        ModsFoldersWithSaves.append(id)
os.chdir(APPDir)

#   Menu
clear()
buffer = 1337
while buffer != "0":
    print("\tWhat are you wanna do today?\n\t1) Export statistics\n\t2) Settings\n\t0) Exit\n\tInput > ", end="")
    buffer = input()
    if buffer == "1":
        clear()
        Exporter.ChooseSaveFile(DeffaultPath, DeffaultMod, APPDir)
    elif buffer == "2":
        clear()
        ModsFoldersWithSaves, DeffaultMod, LanguageFiles = Settings.Settings(ModsFoldersWithSaves, DeffaultMod, LanguageFiles)
    clear()