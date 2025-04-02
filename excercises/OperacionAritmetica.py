from src.tree import Node, BinarySearchTree

class ArithmeticOperationTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.root = None

    def build_tree(self, postfix_expression: str):
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in postfix_expression.split():
            if token not in operators:
                stack.append(Node(int(token)))
            else:
                right = stack.pop()
                left = stack.pop()
                node = Node(token)
                node.left = left
                node.right = right
                stack.append(node)

        self.root = stack.pop()

    def evaluate(self, node: Node) -> float:
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return node.data

        left_val = self.evaluate(node.left)
        right_val = self.evaluate(node.right)

        if node.data == '+':
            return left_val + right_val
        elif node.data == '-':
            return left_val - right_val
        elif node.data == '*':
            return left_val * right_val
        elif node.data == '/':
            return left_val / right_val

    def to_infix(self, node: Node) -> str:
        if node is None:
            return ""

        if node.left is None and node.right is None:
            return str(node.data)

        left_expr = self.to_infix(node.left)
        right_expr = self.to_infix(node.right)

        return f"({left_expr} {node.data} {right_expr})"

if __name__ == "__main__":
    expression = "4 9 7 + 2 * - 3 /"
    tree = ArithmeticOperationTree()
    tree.build_tree(expression)

    result = tree.evaluate(tree.root)
    infix_expression = tree.to_infix(tree.root)

    print(f"Resultado: {result}")
    print(f"Expresión infija: {infix_expression}")