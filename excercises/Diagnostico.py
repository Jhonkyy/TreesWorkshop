import json
from src.tree import Node, BinarySearchTree

class DiagnosticoMedico:
    def __init__(self, arbol):
        self.arbol = arbol

    def hacer_preguntas(self, nodo):
        if "diagnostico" in nodo.data:
            print(f"Diagnóstico: {nodo.data['diagnostico']}")
            return

        respuesta = input(f"{nodo.data['pregunta']} (sí/no): ").strip().lower()
        if respuesta == "sí":
            self.hacer_preguntas(nodo.left)
        elif respuesta == "no":
            self.hacer_preguntas(nodo.right)
        else:
            print("Respuesta no válida. Por favor, responda 'sí' o 'no'.")
            self.hacer_preguntas(nodo)

    def verificar_diagnosticos(self, nodo):
        if "diagnostico" in nodo.data:
            return True

        si_diagnostico = self.verificar_diagnosticos(nodo.left)
        no_diagnostico = self.verificar_diagnosticos(nodo.right)

        return si_diagnostico and no_diagnostico

# Cargar el árbol desde el archivo JSON
with open('arbol_diagnostico_medico.json', 'r', encoding='utf-8') as file:
    arbol_diagnostico = json.load(file)

# Convertir el diccionario en nodos
def dict_to_node(data):
    if not data:
        return None
    node = Node(data)
    node.left = dict_to_node(data.get("si"))
    node.right = dict_to_node(data.get("no"))
    return node

arbol_diagnostico = dict_to_node(arbol_diagnostico)
arbol = BinarySearchTree(arbol_diagnostico)
diagnostico = DiagnosticoMedico(arbol.root)
diagnostico.hacer_preguntas(diagnostico.arbol)

# Verificar que todos los caminos terminan en un diagnóstico
if diagnostico.verificar_diagnosticos(diagnostico.arbol):
    print("Todos los caminos terminan en un diagnóstico.")
else:
    print("Hay caminos que no terminan en un diagnóstico.")