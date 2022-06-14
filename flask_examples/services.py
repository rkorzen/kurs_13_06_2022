
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}

class MathService:

    def handle(self, op, a, b):
        return operations[op](a, b)
