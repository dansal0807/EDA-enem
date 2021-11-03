import re

def convertor(text):
    nums = re.findall('\d+', text)
    return nums

data = []
with open("estatisticas.txt", 'r') as text:
    for line in text:
        converted = convertor(line)
        data.append(converted)

cleaned_data = []
for pairs in data:
    if len(pairs) == 3:
        cleaned_data.append(pairs)

quests_int = []
quests_per = []
for numbers in cleaned_data:
    quests_int.append(numbers[0])

    quest_per = f"{numbers[1]}" + "." + f"{numbers[2]}"
    quests_per.append(quest_per)
