# def count_solutions(P, L):
#     # Function to calculate x^k % P using modular exponentiation
#     def mod_exp(x, k, P):
#         result = 1
#         base = x % P
#         while k > 0:
#             if k % 2 == 1:
#                 result = (result * base) % P
#             base = (base * base) % P
#             k //= 2
#         return result

#     # Precompute all powers x^k % P for k in range 1 to min(L, P-1)
#     power_mod = {k: {x: mod_exp(x, k, P) for x in range(1, P)}
#                  for k in range(1, min(L, P-1) + 1)}

#     count = 0
#     # Check for each k
#     for k in range(1, min(L, P-1) + 1):
#         found_solution = False
#         power_values = set(power_mod[k].values())

#         # Check all combinations (x, y)
#         for x in range(1, P):
#             if found_solution:
#                 break
#             for y in range(1, P):
#                 z_k = (power_mod[k][x] + power_mod[k][y]) % P
#                 if z_k in power_values:
#                     found_solution = True
#                     break

#         if found_solution:
#             count += 1

#     return count
def mod_exp(x, k, P):
    result = 1
    base = x % P
    while k > 0:
        if k % 2 == 1:
            result = (result * base) % P
        base = (base * base) % P
        k //= 2
    return result


def precompute_powers(P):
    power_mod = {}
    for k in range(1, P):
        power_mod[k] = {x: mod_exp(x, k, P) for x in range(1, P)}
    return power_mod


def count_solutions(P, L):
    # Precompute all powers x^k % P for k in range 1 to P-1
    power_mod = precompute_powers(P)

    count = 0
    # Check for each k up to min(L, P-1)
    for k in range(1, min(L, P-1) + 1):
        found_solution = False
        power_values = set(power_mod[k].values())

        # Check all combinations (x, y)
        for x in range(1, P):
            if found_solution:
                break
            for y in range(1, P):
                z_k = (power_mod[k][x] + power_mod[k][y]) % P
                if z_k in power_values:
                    found_solution = True
                    break

        if found_solution:
            count += 1

    return count


# Example usage:
P = [int(i) for i in input().split(" ")]
# print(P)
print(count_solutions(P[0], P[1]))
# 991 945
