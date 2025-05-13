frutas = ['Mango', 'Uva', 'Pera']

# Insert
frutas.insert(1, 'Sandia') # Este metodo agregara un elemento a la lista, en el indice que le indiquemos (Es obligatorio que se indique el indice)
print(frutas)

frutas.insert(-1, 'Durazno') # De igual manera se pueden usar indices negativos, en este caso indicamos que lo queremos al final de la lista.
print(frutas)

# append
frutas.append('Cereza') # Este metodo puede suplir al ejemplo anterior, ya que este agrega al final de la lista sin necesidad de indices.
print(frutas)

# remove
frutas.remove('Mango') # Este metodo removera el elemento que indiquemos, no con el indice, si no con el contenido (en este caso el string).
print(frutas)

# pop
frutas.pop() # El metodo pop, elimina el ultimo elemento de la lista.
print(frutas)

del frutas[2] # Este eliminara un elemento de la lista. Se lo indicaremos con el indice. Y primero se pone la palabra reservada del, no como en los otros metodos que
# es seguido de un punto despues de la lista.
print(frutas)

frutas.clear()
print(frutas)
