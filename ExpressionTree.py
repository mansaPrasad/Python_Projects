#  File: ExpressionTree.py

#  Description:

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/18/21

#  Date Last Modified: 04/19/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        stk = Stack()
        new = Node(expr)
        self.root = new
        ex = expr.split()
        current = self.root

        for i in ex:
            # left parenthesis case
            if i == '(':
                new = Node()
                current.lChild = new
                stk.push(current)
                current = new
            elif i in operators:
                new = Node()
                # set current to operator and push operator into stack
                current.data = i
                stk.push(current)
                # set current equal to the right child
                current.rChild = new
                current = new
            elif i == ')':
                current = stk.pop()

            else:
                if i.isdigit():
                    current.data = int(i)
                else:
                    current.data = float(i)
                current = stk.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        if aNode is None:
            return 0
            # checks if a leaf node
        if aNode.lChild is None and aNode.rChild is None:
            return aNode.data

        left = self.evaluate(aNode.lChild)
        right = self.evaluate(aNode.rChild)

        if aNode.data == '+':
            return left + right
        elif aNode.data == '-':
            return left - right
        elif aNode.data == '*':
            return left * right
        elif aNode.data == '/':
            return left / right
        elif aNode.data == '//':
            return left // right
        elif aNode.data == '%':
            return left % right
        else:
            return left ** right

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        result = ''
        if aNode is not None:
            result += self.pre_order(aNode.lChild)
            result += self.pre_order(aNode.rChild)
            result += str(aNode.data) + ' '
        return result

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        result = ''
        if aNode is not None:
            result += self.post_order(aNode.lChild)
            result += self.post_order(aNode.rChild)
            result += str(aNode.data) + ' '
        return result


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
