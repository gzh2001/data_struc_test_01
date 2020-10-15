from ex_sql_01 import  SqList

def SQLcombine(sql0, sql1):
    SQLc = SqList(sql0.length()+sql1.length())
    c = 0
    while SQLa.length() > 0 and SQLb.length() > 0:
        if SQLa.get(0) > SQLb.get(0):
            SQLc.insert(c, SQLb.get(0))
            SQLb.remove(0)
        else:
            SQLc.insert(c, SQLa.get(0))
            SQLa.remove(0)
        c += 1
    if sql0.isEmpty() == True and sql1.isEmpty() == False:
        for i in range(0, sql1.length()):
            SQLc.insert(SQLc.length(), sql1.get(i))
    else:
        for j in range(0, sql0.length()):
            SQLc.insert(SQLc.length(), sql0.get(j))
    return SQLc

SQLa = SqList(9)
SQLb = SqList(10)
for m in range(0, 19):
    if m < 9:
        SQLa.insert(m, m)
    else:
        SQLb.insert(m-9, m)

SQLcombine(SQLa, SQLb).display()

