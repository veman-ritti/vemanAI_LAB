
def is_variable(x):
    return x[0].islower()


def apply_substitution(x, subst):
    while x in subst:
        x = subst[x]
    return x


def unify(x, y, subst):
    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    if x == y:
        return True

    if is_variable(x):
        subst[x] = y
        return True

    if is_variable(y):
        subst[y] = x
        return True

    return False


def parse_expression(expr):
    expr = expr.strip()

    if "(" not in expr or not expr.endswith(")"):
        return None, []

    predicate = expr[:expr.index("(")].strip()
    arguments = expr[expr.index("(") + 1:-1]

    args = [a.strip() for a in arguments.split(",")]

    return predicate, args


def unification(expr1, expr2):
    p1, args1 = parse_expression(expr1)
    p2, args2 = parse_expression(expr2)

    if p1 is None or p2 is None:
        print("Invalid Expression")
        return

    # Step 1: Check predicate symbols
    if p1 != p2:
        print("Unification Failed: Different predicates")
        return

    # Step 2: Check number of arguments
    if len(args1) != len(args2):
        print("Unification Failed: Different number of arguments")
        return

    # Step 3: Initialize substitution set
    subst = {}

    # Step 4: Unify corresponding arguments
    for x, y in zip(args1, args2):
        if not unify(x, y, subst):
            print("Unification Failed")
            return

    # Step 5: Apply substitutions
    print("\nUnification Successful!")
    print("Substitution Set:")

    if not subst:
        print("No substitutions required")
    else:
        for var, value in subst.items():
            print(var, "=", apply_substitution(value, subst))


# Main Program
expr1 = input("Enter first expression: ")
expr2 = input("Enter second expression: ")

unification(expr1, expr2)
