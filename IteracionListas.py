frutas = ['Mango', 'Fresa', 'Uva']

for fruta in frutas: # En este solo iteraremos todos los elementos de la lista
    print(fruta)

for fruta in enumerate(frutas): # En este nos iterara los elementos de la lista pero le agregara un indice a cada elemento
    print(fruta)

for indice, fruta in enumerate(frutas): # En el ejemplo anterior nos imprimia los elemntos en tuplas. Si queremos que los imprima, debemos crear un elemento mas
    # en la cabecera del for para que a cada uno se le asigne un elemento, por lo cual el primer elemento tomara el valor del indice y el segundo el de la fruta.
    print(indice, fruta)

for indice, fruta in enumerate(frutas): # En este solo indicaremos que se imprima el segundo elemento de la dupla, el cual sera la fruta.
    print(fruta)

for indice, fruta in enumerate(frutas): # En este solo sera imprimir el indice.
    print(indice)

for fruta in enumerate(frutas): # Tambien podemos usar corchetes para indicar el indice de la tupla y que imprima ese elemento, en este caso 0 tomara el elemento del
    # indice de las frutas
    print(fruta[0])

for fruta in enumerate(frutas): # Y en este ultimo tomara las frutas.
    print(fruta[1])
