# 🧠 Ejercicio 1: Árbol de Decisiones para Diagnóstico Médico
## 🎯 Objetivo
Simular un sistema de diagnóstico médico que realiza preguntas binarias (sí/no) para llegar a una conclusión diagnóstica.

### 🏗 Estructura del Árbol
Cada nodo es una pregunta del tipo "¿Tiene fiebre?", y cada hoja es un diagnóstico como "Gripe", "Covid-19", "Alergia", etc.

### 💻 Tareas a realizar
1. Implementar una función que recorra el árbol haciendo preguntas al usuario y lo lleve a un diagnóstico.

2. Implementar recorrido postorden para verificar que todos los caminos terminan en un diagnóstico.

3. (Opcional) Permitir actualizar el árbol si el diagnóstico no fue correcto (el usuario puede añadir una nueva pregunta/diagnóstico).

----

# 🎲 Ejercicio 2: Árbol de Juego de Adivinanzas
## 🎯 Objetivo
Simular un juego interactivo donde el programa hace preguntas hasta adivinar lo que el usuario piensa. Si no adivina, se enriquece el árbol con una nueva pregunta y respuesta.

## 💻 Tareas a realizar
1. Implementar recorrido preorden para mostrar todas las posibles preguntas.

2. Implementar el juego interactivo que recorre el árbol según las respuestas del usuario.

3. el sistema falla, permitir al usuario agregar:

   * El objeto que estaba pensando.

   * Una nueva pregunta para diferenciarlo del nodo fallido.

4. Guardar el árbol actualizado en un archivo (usando pickle o JSON).

---

# ➗ Ejercicio 3: Árbol de Operaciones Aritméticas
## 🎯 Objetivo
Dada una expresión matemática en notación postfija (RPN), construir un árbol binario y evaluar su valor. También mostrar la expresión en notación infija.

## 🧮 Ejemplo de entrada:
Expresión postfija:
* 3 4 + 2 * 7 /


## 💻 Tareas a realizar
1. Construir el árbol desde la expresión postfija.

2. Implementar recorrido postorden para evaluar el resultado.

3. Implementar recorrido inorden para reconstruir la expresión en notación infija con paréntesis:
   * (( 3+ 4) * 2) / 7 

4. (Opcional) Permitir convertir expresiones en notación infija a árbol directamente.