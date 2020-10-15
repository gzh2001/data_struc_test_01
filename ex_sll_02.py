from ex_sll_01 import LinkList

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
SLLa = LinkList()
SLLb = LinkList()
SLLc = LinkList()
SLLa.creat(a, True)
SLLb.creat(b, True)

c = []
while SLLa.length() != 0 and SLLb.length() != 0:
    if SLLa.get(0) <= SLLb.get(0):
        c.append(SLLa.get(0))
        SLLa.remove(0)
    else:
        c.append(SLLb.get(0))
        SLLb.remove(0)
SLLc.creat(c, True)

while  SLLa.isEmpty() is not True:
    SLLc.creat_tail([SLLa.get(0)])
    SLLa.remove(0)
while SLLb.isEmpty() is not True:
    SLLc.creat_tail([SLLb.get(0)])
    SLLb.remove(0)
SLLc.display()


