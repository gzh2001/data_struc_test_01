from ex_sql_01 import  SqList


SQLa = SqList(9)
SQLb = SqList(10)
for m in range(19):
    if m < 9:
        SQLa.insert(m, m)
    else:
        SQLb.insert(m-9, m)
        

SQLc = SqList(SQLa.length() + SQLb.length())
print(SQLa.length() + SQLb.length())
c = 0
while SQLa.length() > 0 and SQLb.length() > 0:
    if SQLa.get(0) > SQLb.get(0):
        SQLc.insert(c, SQLb.get(0))
        SQLb.remove(0)
    else:
        SQLc.insert(c, SQLa.get(0))
        SQLa.remove(0)
    c += 1
if SQLa.isEmpty() == True and SQLb.isEmpty() == False:
    for i in range(0, SQLb.length()):
        SQLc.insert(SQLc.length(), SQLb.get(i))
else:
    for j in range(0, SQLa.length()):
        SQLc.insert(SQLc.length(), SQLa.get(j))
