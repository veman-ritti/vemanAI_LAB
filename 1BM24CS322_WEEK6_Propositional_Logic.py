
from itertools import product

def implies(a, b):
    return (not a) or b

# Generate all possible truth assignments
print("P Q R | Q->P | P->~Q | QvR | KB")
print("---------------------------------------")

models = []

for P, Q, R in product([True, False], repeat=3):

    s1 = implies(Q, P)
    s2 = implies(P, not Q)
    s3 = Q or R

    kb = s1 and s2 and s3

    models.append((P, Q, R, kb))

    print(f"{int(P)} {int(Q)} {int(R)} |"
          f"  {int(s1)}   |"
          f"   {int(s2)}   |"
          f"  {int(s3)}  |"
          f" {int(kb)}")

# Display models where KB is true
print("\nModels where KB is TRUE:")
for P, Q, R, kb in models:
    if kb:
        print(f"P={int(P)}, Q={int(Q)}, R={int(R)}")

# Check entailment
queries = {
    "R": lambda P, Q, R: R,
    "R -> P": lambda P, Q, R: implies(R, P),
    "Q -> R": lambda P, Q, R: implies(Q, R)
}

print("\nENTAILMENT RESULTS")

for name, query in queries.items():

    entails = True

    for P, Q, R, kb in models:
        if kb and not query(P, Q, R):
            entails = False
            break

    print(f"KB entails {name}: {entails}")
