"""
Evaluate.py
Evaluate an infix expression. Dijkstra's two stack 
algorithm:
- push value onto the stack
- push operator onto the operator stack 
- ignore left parenthesis
- right parenthesis, pop operator and two values; push the result of applying that operator to those values onto the operand stack. 
"""
from collections import deque
class Evaluate:
    ops = deque()  # operand stack: +, *
    vals = deque()  # integer stack: 3, 1
    @classmethod
    def eval(cls, expression: str) -> int:
        for i in range(len(expression)):
            s = expression[i]
            if s == '(': continue 
            elif s == '+': cls.ops.append(s) 
            elif s == '*': cls.ops.append(s) 
            elif s == ')':
                op = cls.ops.pop()
                if op == '+': 
                    cls.vals.append(cls.vals.pop() + cls.vals.pop())
                elif op == '*':
                    cls.vals.append(cls.vals.pop() * cls.vals.pop())
            else:
                cls.vals.append(int(s))

        print(cls.vals.pop())

def main():
    Evaluate.eval('(1+((2+3)*(4*5)))')

if __name__ == '__main__':
    main()

