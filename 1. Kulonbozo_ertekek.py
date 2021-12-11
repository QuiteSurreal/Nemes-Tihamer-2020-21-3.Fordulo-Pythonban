from sys import stdin, stdout

def main():
    hanyszam, maxszam = map(int, stdin.readline().split())
    szamok = (list(map(int, stdin.readline().split())))
    kerdesek = int(stdin.readline())
    khossz = []
    megoldasok = []
    for i in range(kerdesek):
        khossz.append(list(map(int, stdin.readline().split())))
    uq = list(set(szamok))
    for i in range(kerdesek):
        megoldasszam = 0
        for j in range(len(uq)):
            if khossz[i][0] <= uq[j] <= khossz[i][1]:
                megoldasszam += 1
            if uq[j] >= khossz[i][1]:
                break
        megoldasok.append(megoldasszam)
    for i in range(len(megoldasok)):
        stdout.write(str(megoldasok[i]) + "\n")
main()