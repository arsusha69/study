import numpy as np

pay = np.array([
    [0.575, 0.075, 0.075, 0.075],
    [0.5, 0.575, 0.075, 0.075],
    [-0.075, 0.5, 0.575, 0.075],
    [-0.075, -0.075, 0.5, 0.575]
])

a_cumul_sum = np.zeros(4)
b_cumul_sum = np.zeros(4)
a_used_strats = np.zeros(4)
b_used_strats = np.zeros(4)

iterations = 50

a_strat = 1
prev_a_strat = 1
b_strat = 1
value = 0

print(
    f"{'Итерация':<10}{'Ai':<5}{'B1':<9}{'B2':<9}{'B3':<9}{'B4':<8}{'Bi':<5}{'A1':<9}{'A2':<9}{'A3':<9}{'A4':<9}{'V-':<9}{'V+':<9}{'V':<9}")
print('-' * 120)

for i in range(iterations):
    a_cumul_sum += pay[a_strat]
    b_strat = np.argmin(a_cumul_sum)
    b_cumul_sum += pay[:, b_strat]

    a_used_strats[a_strat] += 1
    b_used_strats[b_strat] += 1

    v_low = a_cumul_sum[b_strat] / (i + 1)
    prev_a_strat = a_strat
    a_strat = np.argmax(b_cumul_sum)
    v_high = b_cumul_sum[a_strat] / (i + 1)
    value = (v_low + v_high) / 2

    b_values = ' '.join([f"{val:<8.2f}" for val in a_cumul_sum])
    a_values = ' '.join([f"{val:<8.2f}" for val in b_cumul_sum])
    print(
        f"{i + 1:<10}{prev_a_strat + 1:<5}{b_values}{b_strat + 1:<5}{a_values}{v_low:<8.2f}{v_high:<8.2f}{value:<8.2f}")

print(f'Смешанная стратегия игрока A: {a_used_strats / iterations}')
print(f'Смешанная стратегия игрока B: {b_used_strats / iterations}')
print(f'Цена игры: {value:<8.2f}')