import json
from src.tree import Node, BinarySearchTree

class Adivinanza:
    def __init__(self, arbol):
        self.arbol = arbol

    def hacer_preguntas(self, nodo):
        if "adivinanza" in nodo.data:
            print(f"Adivinanza: {nodo.data['adivinanza']}")
            return

        if "pregunta" not in nodo.data:
            print("Error: Nodo sin pregunta.")
            return

        respuesta = input(f"{nodo.data['pregunta']} (si/no): ").strip().lower()
        if respuesta == "si":
            self.hacer_preguntas(nodo.left)
        elif respuesta == "no":
            self.hacer_preguntas(nodo.right)
        else:
            print("Respuesta no válida. Por favor, responda 'si' o 'no'.")
            self.hacer_preguntas(nodo)

    def verificar_respuestas(self, nodo):
        if "adivinanza" in nodo.data:
            return True

        si_respuesta = self.verificar_respuestas(nodo.left)
        no_respuesta = self.verificar_respuestas(nodo.right)

        return si_respuesta and no_respuesta

if __name__ == "__main__":
    # Cargar el árbol desde el archivo JSON
    with open('arbol_adivinanzas.json', 'r', encoding='utf-8') as file:
        arbol_adivinanzas = json.load(file)

    # Convertir el diccionario en nodos
    def dict_to_node(data):
        if not data:
            return None
        node = Node(data)
        node.left = dict_to_node(data.get("si"))
        node.right = dict_to_node(data.get("no"))
        return node

    arbol_adivinanzas = dict_to_node(arbol_adivinanzas)
    arbol = BinarySearchTree(arbol_adivinanzas)
    adivinanza = Adivinanza(arbol.root)
    adivinanza.hacer_preguntas(adivinanza.arbol)

    # Verificar que todos los caminos terminan en una respuesta
    if adivinanza.verificar_respuestas(adivinanza.arbol):
        print("Todas las rutas terminan en una adivinanza.")
    else:
        print("Hay rutas que no terminan en una adivinanza.")