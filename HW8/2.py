text = input("Enter some text: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

percentage_dict = {}

for char, count in char_count.items():
    percentage = (count / len(text)) * 100
    percentage_dict[char] = percentage

for char, percentage in percentage_dict.items():
    print(f"{char}    {percentage:.2f}%")