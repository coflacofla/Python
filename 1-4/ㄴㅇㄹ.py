for i in range(8):
    print('*'*i)

for i in range(8)[::-1]:
    print('*'*i)

for i in range(8):
    print(f'{"*"*i:>8}')

for i in range(1, 14, 2):
    print(f'{"*"*i:^13}')

temp = list(range(1, 8, 2)) + list(range(1, 7, 2))[::-1]
for i in temp:
    print(f'{"*"*i:^7}')

for i in range(8):
    print(f'{" "*(8-i)}{"*"*i}')

for i in range(1, 14, 2):
    print(f'{" "*(13-i//2)}{"*"*i}{" "*(13-i//2)}')

for i in temp:
    print(f'{" "*(7-i//2)}{"*"*i}{" "*(7-i//2)}')
