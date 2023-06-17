import openpyxl as op


def InsertExcel(ws, _val, line):
    col = 1
    for val in _val:
        ws.cell(row=line, column=col, value=val)
        col += 1


def readLog():
    file = open(file=r"C:\\Users\\30309\\Desktop\\GovSpider\\Spider\\Seleium\\msg_xpath\\log.txt", mode="r",
                encoding="utf-8")
    lines = file.readlines()
    file.close()
    return lines


def writeLog(have_head, prevLine):
    file = open(file=r"C:\\Users\\30309\\Desktop\\GovSpider\\Spider\\Seleium\\msg_xpath\\log.txt", mode="w",
                encoding="utf-8")
    file.write('HEAD:' + str(have_head) + '\n' + 'endLine:' + str(prevLine))
    file.close()
