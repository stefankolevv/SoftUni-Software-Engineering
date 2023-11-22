import re

racers = input().split(', ')
racers_dict = {racer: 0 for racer in racers}
pattern = re.compile(r'{A-Z}{a-z}+')

while True:
    input_line = input()
    if input_line == 'end of race':
        break
    else:
        pass

    match = pattern.findall(input_line)
    name = ''.join([char for char in match if char.isalpha()])
    distance = sum([int(char) for char in match if char.isdigit()])

    if name in racers_dict:
        racers_dict[name] += distance

sorted_racers = dict(sorted(racers_dict.items(), key=lambda x: -x[1]))

top_3_racers = list(sorted_racers.keys())[:3]

places = ["1st", "2nd", "3rd"]

for i in range(len(top_3_racers)):
    place = places[i]
    racer = top_3_racers[i]
    distance = sorted_racers[racer]
    print(f"{place} place: {racer}")
