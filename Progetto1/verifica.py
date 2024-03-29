from Progetto1.util import *
from Progetto1.suffix import *
from Progetto1.my_list import *


rl = randList(1, 10, 3)
rkl = rand_keys_list(3, 1, 10)
rs = random_string(5)
rwl = rand_words_list(10, 3, 7)
rd = rand_dict(12)

# test di append(x) + clear()
print("Creo l_uno e l_due e verifico che l'append sia uguale su entrambi:")
l_uno = MyList()
l_uno.append("d")
l_uno.append(2)
l_uno.extend("abc")
l_uno[len(l_uno):] = [4]
print("l_uno:", l_uno)
l_due = MyList(l_uno)
print("l_due:", l_due)
l_due.append("dieci")
print("l_due con append di dieci:", l_due, "!= l_uno:", l_uno)
l_uno.append("dieci")
print("l_uno con append di dieci:", l_uno, "== l_due:", l_due)
l_uno.append(rl)
print("append con lista causale su l_uno:", l_uno)
l_uno.clear()
l_uno.append(rkl)
print("clear + append con random key list:", l_uno)
l_uno.append(rs)
print("append di stringa causale:", l_uno)
l_uno.append(rwl)
print("append di parole causali", l_uno)
l_uno.append(rd)
print("append di un dizionario causale", l_uno)
l_uno.clear()
l_due.clear()
print("clear su l_uno e l_due: l_uno:", l_uno, "== l_due:", l_due)
# test di insert(i,x)
# test con indice non definito
# l_uno.insert(3, 4)
l_uno.append(5.4)
l_uno.append(3.2)
l_due = MyList(l_uno)
print("Ridefinisco l_uno:", l_uno, "e l_due:", l_due)
l_uno.insert(0, "bc")
l_due.insert(0, "bc")
print("Testo la insert in posizione 0: l_uno:", l_uno, "l_due: ", l_due)
l_uno.insert(3, 22)
l_due.insert(3, 22)
print("Testo la insert in posizione 3: l_uno:", l_uno, "l_due: ", l_due)
l_uno.insert(1, 50)
l_due.insert(1, 50)
print("Testo la insert in posizione 1: l_uno:", l_uno, "l_due: ", l_due)
l_uno.insert(-2, 99)
l_due.insert(-2, 99)
print("Testo la insert con indici negativi -2: l_uno:", l_uno, "l_due: ", l_due)
# test remove(x) e __delitem__
l_uno.remove(50)
l_due.remove(50)
print("Testo la rimozione di 50 : l_uno:", l_uno, "l_due: ", l_due)
l_uno.remove("bc")
l_due.remove("bc")
print("Testo la rimozione di bc: l_uno:", l_uno, "l_due: ", l_due)
l_uno.remove(22)
l_due.remove(22)
#del l_uno[2:3]
#del l_due[2:3]
#print("Testo la rimozione di 3.2 con __delitem__: l_uno:", l_uno, "l_due: ", l_due)
# test di pop([i]) ed extend(iterable), count(x), reverse(), __setitem__,  index(x[, start[, end]]) e __getitem__
l_uno.extend(rl)
l_due.extend(rl)
print("Estendo le due liste con una lista causale: l_uno:", l_uno, "l_due: ", l_due)
l_uno.reverse()
l_due.reverse()
print("Ne stampo il reverse: l_uno", l_uno, "l_due: ", l_due)
l_uno[0] = 3
l_uno[2] = 3
l_uno[4] = 3
l_due[0] = 3
l_due[2] = 3
l_due[4] = 3
print("Imposto tre 3 alle liste con l'operatore __setitem__: l_uno:  ", l_uno, "l_due: ", l_due)
print("Stampo il numero di 3 nelle liste: l_uno: ", l_uno.count(3), "l_due: ", l_due.count(3))
print("Stampo index(3): l_uno:", l_uno.index(3), "l_due: ", l_due.index(3))
print("Stampo index(3,1,3): l_uno:", l_uno.index(3, 1, 3), "l_due: ", l_due.index(3, 1, 3))
print("Stampo index(3.2, -4, -1) per indici negativi: l_uno:", l_uno.index(3.2, -4, -1), "l_due: ", l_uno.index(3.2, -4, -1))
l_uno.pop()
l_due.pop()
print("Ne faccio il pop(): l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(0)
l_due.pop(0)
print("Faccio il pop in posizione 0: l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(2)
l_due.pop(2)
print("Faccio il pop in posizione 2: l_uno:", l_uno, "l_due: ", l_due)
l_uno.pop(-2)
l_due.pop(-2)
print("Faccio il pop in posizione -2: l_uno:", l_uno, "l_due: ", l_due)
# test di copy()
l_uno.insert(0, rl)
l_due.insert(0, rl)
l_tre = l_uno.copy()
l_quattro = l_due[:]
print("Creo due copie di l_uno e l_due: l_tre dopo aver inserito una "
      "lista in posizione 0:\n l_tre = l_uno.copy(): ", l_tre, "l_quattro = l_due[:]: ", l_quattro)
l_tre[2] = 44
l_tre[0][1] = 33
l_quattro[2] = 44
l_quattro[0][1] = 33

print("Modifico l_tre[2]e l_tre[0][1] anche su l_quattro e"
      " stampo le sequenze: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)


print("Stampo usando getitem l_tre[0][1]:", l_tre[0][1])

# test di  len, e bool

print("Restituisco la lungezza di l_uno:", len(l_uno), "l_due: ", len(l_due))
l_tre.clear()
print("Restituisco bool di l_uno, l_due e l_tre(dopo aver fatto il clear()): \n"
      " l_uno:", bool(l_uno), "l_due: ", bool(l_due), "l_tre: ", bool(l_tre))
del l_quattro[:]
print("Faccio il clear di l_quattro con del l_quattro[:] l_quattro:", l_quattro)
# test di __add__ e __iadd__
l_tre, l_quattro = l_uno, l_due
l_tre += [10, 23]
l_quattro += [10, 23]
print("Faccio una copia di l_uno e l_due in l_tre e l_quattro e poi"
      "l_tre += [10,23] = l_quattro: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)
l_tre = l_tre + [11, 24]
l_quattro = l_quattro + [11, 24]

print("Ora faccio l_tre = l_tre + [11, 24] = l_quattro "
      "e stampo il risultato: \n l_uno:", l_uno, "l_due: ", l_due, "\nl_tre:", l_tre, "l_quattro", l_quattro)

# test di __le__ , __lt__ , __eq__ , ___ne__, __ge__, __gt__

print("Stampo l_uno != l_due: ", l_uno != l_due)
print("Stampo l_uno == l_due: ", l_uno == l_due)
print("Stampo l_uno >= l_due: ", l_uno >= l_due)
print("Stampo l_uno > l_due: ", l_uno > l_due)
print("Stampo l_uno < l_due: ", l_uno < l_due)
print("Stampo l_uno <= l_due: ", l_uno <= l_due)
print("Rimuovo da l_due il 3 e modifico 23 a 33 e rifaccio i test:")
l_due.remove(3)
l_due[3] = 33
print("Stampo l_uno != l_due: ", l_uno != l_due)
print("Stampo l_uno == l_due: ", l_uno == l_due)
print("Stampo l_uno >= l_due: ", l_uno >= l_due)
print("Stampo l_uno > l_due: ", l_uno > l_due)
print("Stampo l_uno < l_due: ", l_uno < l_due)
print("Stampo l_uno <= l_due: ", l_uno <= l_due)

# test contains
print("Testo se 3  è contenuto in l_uno")
print(3 in l_uno)
print("Testo se 33  è contenuto in l_uno")
print(33 in l_uno)
print("Testo la funzione stampa suffissi (iterativa) sulla 4 liste create precedentemente")
print("l_uno:", l_uno)
print("Suffissi list_uno")
print(ssi(l_uno))
print("l_due:", l_due)
print("Suffissi list_due")
print(ssi(l_due))
print("l_tre:", l_tre)
print("Suffissi list_tre")
print(ssi(l_tre))
print("l_quattro:", l_quattro)
print("Suffissi list_quattro")
print(ssi(l_quattro))

l_test = MyList()
l_test.extend((123, 300))
l_test.reverse()
print("l_test = ", l_test)

print("Test iterativo")
print(ssi(l_test))
print("Test Ricorsivo")
print(ssr(l_test))
print("Lista Test a cui ho aggiunto 100:")
l_test.insert(1, 100)
print(l_test)


print("Lista Test Interi -- Test key=abs:")
test = randList(-20000, 0, 10000)
rw_test = MyList()
rw_test.extend(test)
print(rw_test)
rw_test.sort(key=abs)
print("Lista Test Ordinata")
print(rw_test)


print("Lista Test Stringhe preordinamento:")
test = rand_words_list(100, 2, 22)
rw_test = MyList()
rw_test.extend(test)
print(rw_test)
rw_test.sort()
print("Lista Test Ordinata:")
print(rw_test)


class Test:

    def __init__(self, **arg):
        self._1 = arg.get('uno')
        self._2 = arg.get('due')
        self._3 = arg.get('tre')

    def __str__(self):
        return "UNO: "+str(self._1)+" - DUE: "+str(self._2)+" - TRE: "+str(self._3)


def key1(test):
    if type(test) is Test:
        return test._1
    else:
        raise TypeError("Il tipo non è supportato.")


def key2(test):
    if type(test) is Test:
        return test._2
    else:
        raise TypeError("Il tipo non è supportato.")


def key3(test):
    if type(test) is Test:
        return test._3
    else:
        raise TypeError("Il tipo non è supportato.")


lista_test = MyList()
test_1 = Test(uno=10, due=10, tre=10)
test_2 = Test(uno=32, due=32, tre=65)
test_3 = Test(uno=543, due=1, tre=43)
test_4 = Test(uno=65, due=45, tre=7)
lista_test.append(test_1)
lista_test.append(test_2)
lista_test.append(test_3)
lista_test.append(test_4)
print("Stampa di lista test con nuovi elementi:")
print(lista_test)
print("Stampa di lista test con funzione key che ordina in base al terzo attributo:")
lista_test.sort(key=key3)
print(lista_test)

