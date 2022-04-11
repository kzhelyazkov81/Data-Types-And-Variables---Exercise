number_of_characters = int(input())
total_sum = 0

for _ in range(number_of_characters):
    letter = input()
    total_sum += ord(letter)

print(f'The sum equals: {total_sum}')
