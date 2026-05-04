# ============================================================
# Parcial 2 - Estructura de Datos I
# Código base final
# ============================================================


# ============================================================
# Punto 1: Lista Circular - Josephus modificado
# ============================================================

class NodoCircular:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoCircular(dato)

        if not self.head:
            self.head = nuevo
            nuevo.next = self.head
            return

        actual = self.head
        while actual.next != self.head:
            actual = actual.next

        actual.next = nuevo
        nuevo.next = self.head

    def crear_lista(self, n):
        for i in range(1, n + 1):
            self.insertar_final(i)

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        resultado = []
        actual = self.head

        while True:
            resultado.append(str(actual.dato))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(resultado) + " -> (ciclo)")

    def josephus_modificado(self, m):
        m=input("Digite los saltos: ")
        n=input("Digite la cantidad de nodos: ")
        if self.head is None:
           return
        
        for i in range(int(n-1)):
            new_node=NodoCircular(i)
            new_node.next=new_node

        new_node.next=self.head
        
        prev=None
        current=self.head

        while current.nex != current:
            for i in range(m-1):
                current=current.next

            deleted=current
            sgte=current.next
            prev.next=current.next
            current=sgte

            if deleted.data%5==0:
                current=current.next
            
        return current.data
    

# ============================================================
# Punto 2: Lista Simple - Método único
# ============================================================

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.next = None


class ListaSimple:
    def __init__(self):
        self.head = None

    def insertar_final(self, dato):
        nuevo = NodoSimple(dato)

        if not self.head:
            self.head = nuevo
            return

        actual = self.head
        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def mostrar(self):
        if not self.head:
            print("Lista vacía")
            return

        actual = self.head
        resultado = []

        while actual:
            resultado.append(str(actual.dato))
            actual = actual.next

        print(" -> ".join(resultado) + " -> None")

    def partir_voltear_intercalar(self, lista):
        if self.head is None:
            return
        
        lento=self.head
        rapido=self.head

        while rapido:
            lento=lento.next
            rapido = rapido.next.next
            c+=1
        
        mitad=lento

        current=mitad
        prev=None

        while current:
            sgte=current.next
            current.next=prev
            prev.next=current.next
            prev=current

        if c%2!=0:
            prev=None
            current=mitad

            while current.next:
                sgte=current.next.next
                prev.next=current
                current.next=prev.next
                prev=prev.next.next
                current=sgte

        return lista


# ============================================================
# Pruebas base
# ============================================================

if __name__ == "__main__":

    print("===== Punto 1 =====")
    lista_c = ListaCircular()
    lista_c.crear_lista(7)
    lista_c.mostrar()

    sobreviviente = lista_c.josephus_modificado(3)
    print("Sobreviviente:", sobreviviente)


    print("\n===== Punto 2 =====")
    lista_s = ListaSimple()

    for x in [1, 2, 3, 4, 5, 6]:
        lista_s.insertar_final(x)

    lista_s.mostrar()

    lista_s.partir_voltear_intercalar()

    print("Resultado:")
    lista_s.mostrar()