import os
import openpyxl

clear = lambda: os.system('cls')

def ChooseSaveFile(DeffaultPath, DeffaultMod, APPDir):
    os.chdir(DeffaultPath + DeffaultMod)
    buff = os.listdir()
    print("\tChoose save file")
    for i in buff:
        print("\t",buff.index(i) + 1, i)
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
    while buffer != "alienBases:\n":    # Поиск конца списка bases и начало alienBases и начало сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "alienMissions:\n":    # Поиск конца списка alienBases в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "discovered:\n":    # Поиск начала списка discovered в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    while buffer != "poppedResearch:\n":    # Поиск конца списка discovered в сохранении
        buffer = f.readline()
    Datapoints.append(f.tell())
    ws.append(Datapoints)
    #Вывод инф-ии о базах
    for col in ws.columns:
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
    wb.save("EXPORT.xlsx")
    return 0