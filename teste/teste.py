n = int(input())

for j in range(n):
    x = input().split()
    lista = []
    s = ''

    for i in range(len(x)):
        lista.append(x[i])

    lista = sorted(set(lista))

    for i in range(len(lista)):
        s += lista[i]
        if i < (len(lista) - 1):
            s += ' '

    print(s)