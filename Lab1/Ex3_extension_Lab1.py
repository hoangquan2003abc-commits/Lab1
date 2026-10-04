left_operands = [-5, 0, 5, 7.5]
right_operand = 2

def safe_sqrt(x):
    return f"{x ** 0.5:.3f}" if x >= 0 else "error"

header = (f"{'a':>5} | {'a + 2':>7} | {'a - 2':>7} | {'a * 2':>7} | "
          f"{'a / 2':>7} | {'a // 2':>7} | {'a ** 2':>7} | {'sqrt(a)':>8}")
print(header)
print("-" * len(header))

for a in left_operands:
    print(f"{a:>5} | {a + right_operand:>7} | {a - right_operand:>7} | "
          f"{a * right_operand:>7} | {a / right_operand:>7} | "
          f"{a // right_operand:>7} | {a ** right_operand:>7} | "
          f"{safe_sqrt(a):>8}")