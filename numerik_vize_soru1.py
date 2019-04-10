'''
ax+by=c
dx+ey=f

Verilen denklem sisteminin kökü olup olmadığını, varsa kaç kökü olduğunu çıktı olarak veren kodu yazınız.
'''
if a/d == b/e:
    if c/f == a/d:
        print("Sonsuz kök var.")
    else:
        print("Hiç kök yok.")
else:
    print("1 tane kökü var.")
