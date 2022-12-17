import os
import openpyxl

clear = lambda: os.system('cls')

def ChooseSaveFile(DeffaultPath, DeffaultMod, APPDir):
    os.chdir(DeffaultPath + DeffaultMod)
    buff = os.listdir()
    if buff != []:
        print("\tChoose save file")
        for i in buff:
            print("\t",buff.index(i) + 1, i)
        print("\tInput > ", end="")
        Export(buff[int(input()) - 1], APPDir)
    return 0

def Export(savefile, APPDir):
    f = open(savefile)
    os.chdir(APPDir)
    wb = openpyxl.Workbook()
    ws = wb.active
    Datapoints = [] # Индексы 0 и 1 отвечают за список Bases, 1 и 2 за AlienBases, 3 и 4 за discovered
    buffer = ""
    while buffer != "bases:\n":    # Поиск начала списка bases в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "alienBases:\n" and buffer != "alienMissions:\n":    # Поиск конца списка bases и начало alienBases и начало сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "alienMissions:\n":    # Поиск конца списка alienBases в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "discovered:\n":    # Поиск начала списка discovered в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    buffer = f.readline()
    while buffer.find(":") == -1:    # Поиск конца списка discovered в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    #Поиск строчек о хар-ках (В модификациях любят играться с изменением хар-ик)
    Stats = ["", "Soliders"]
    Found = 0
    f.seek(Datapoints[0])
    buffer = f.readline()
    while f.tell() <= Datapoints[1]:
        if "        currentStats:\n" == buffer:
            Found = 1
        elif Found == 1 and buffer[:13] != "        rank:":
            Stats.append(buffer[:buffer.index(":")].replace(" ", ""))
        elif buffer[:13] == "        rank:":
            break
        buffer = f.readline()
    #Вывод инф-ии о базах
    f.seek(Datapoints[0])
    buffer = f.readline()
    while f.tell() <= Datapoints[1]:
        if "  - lon:" == buffer[0:8]:
            f.readline()
            buffer = f.readline()[10:]
            ws.append([buffer])
            ws.append(Stats)
            buffer = f.readline()
            while "  - lon:" != buffer[0:8] and f.tell() <= Datapoints[1]:
                buffer = f.readline()
                if "        name:" == buffer[0:13]:
                    stroka = ["", buffer[14:]]
                    while buffer != "        currentStats:\n":
                        buffer = f.readline()
                    buffer = f.readline()
                    while buffer[:13] != "        rank:":
                        buffer = f.readline()
                        stroka.append(buffer[buffer.index(":") + 1:])
                    ws.append(stroka)
                if buffer == "    items:\n":
                    ws.append(["", "Storage"])
                    buffer = f.readline()
                    while buffer[:15] != "    scientists:":
                        ws.append(["", "", buffer[6:]])
                        buffer = f.readline()
    ws.append([""])
    ws.append([""])
    # Вывод инф-ию о активных базах
    ws.append(["AlienBases", "race", "deployment", "startMonth"])
    f.seek(Datapoints[1])
    buffer = f.readline()
    while f.tell() <= Datapoints[2] - 1:
        if "  - lon:" == buffer[0:8]:
            while "    race:" != buffer[:9]:
                buffer = f.readline()
            stroka = ["", buffer[9:]]
            while "    deployment:" != buffer[:15]:
                buffer = f.readline()
            stroka.append(buffer[16:])
            buffer = f.readline()
            stroka.append(buffer[16:])
            ws.append(stroka)
        buffer = f.readline()
    ws.append([""])
    ws.append([""])
    # Вывод инф-ии об изученных технологиях
    ws.append(["discovered"])
    f.seek(Datapoints[3])
    buffer = f.readline()
    while buffer != "poppedResearch:\n" and f.tell() <= Datapoints[4] - 1 and buffer != "ufopediaRuleStatus:\n":
        ws.append(["", buffer[4:]])
        buffer = f.readline()
    for col in ws.columns:  # Выставляет ширину для столбцов
        max_length = 0
        column = col[0].column_letter  # Получить букву столбца
        for cell in col:
            try:  # Необходимо для избегания потенциальных ошибок
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column].width = adjusted_width
    f.close()
    buffer = os.listdir()
    num = 0
    while ("EXPORT" + str(num) + ".xlsx") in buffer:
        num += 1
    wb.save("EXPORT" + str(num) + ".xlsx")
    return 0