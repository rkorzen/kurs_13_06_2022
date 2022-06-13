a = 1   # globalna


def foo():
    global b
    b = 2   # z punktu widzenia funkcji foo - b jest w przestrzeni lokalnej, a w globalnej

    def bar():  # to z foo to moze byc tez przestrzen domykajaca - stad domkniecia - clojures
        # nonlocal b

        b = 10
        c = 3  # z pnkt. widz. funkcji bar - c jest w lokalnej
               # a - jest w globalnej
               # b - nonlocal

        locals()
        globals()

print(dir(__builtins__))

x = [1, 2, 3, 4, 5]
print(x[slice(1, 6, 2)])
