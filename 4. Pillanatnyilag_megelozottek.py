from sys import stdin, stdout

def main():
    emberek, maxpont = map(int, stdin.readline().split())
    pontok = list(map(int, stdin.readline().split()))
    elertpont = []
    for i in range(emberek):
        b = pontok.copy()
        del b[i+1:len(pontok)]
        b.sort()
        pont = b.index(pontok[i])
        elertpont.append(pont)
    for i in range(len(elertpont)):
        stdout.write(str(elertpont[i]) + " ")
main()
