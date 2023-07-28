from collections import defaultdict
MAX_LEN = 8
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
chess_positions = defaultdict(list)
for ind, key in enumerate(keys):
    if ind % 2 == 0:
        for i in range(MAX_LEN):
            if i % 2 == 0:
                chess_positions[key].append('black')
            else:
                chess_positions[key].append('white')
    else:
        for i in range(MAX_LEN):
            if i % 2 == 0:
                chess_positions[key].append('white')
            else:
                chess_positions[key].append('black')
print(chess_positions)
char = input("Введіть літеру позиції від a до h:\t")
num = int(input("Введіть число позиції від 1 до 8:\t"))
result = chess_positions[char][num-1]
print(f"Результат: {result}")