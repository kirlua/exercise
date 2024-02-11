list_of_fish = [
    "flounder", "sole", "blue cod", "snapper", "terakihi", "john dory",
    "red cod"
]

def find_maximum(lst, start=0, max_word=''):
    if start == len(lst):
        return max_word
    if len(lst[start]) > len(max_word):
        max_word = lst[start]
    return find_maximum(lst, start + 1, max_word)

max_fish = find_maximum(list_of_fish)
  #lst can be used as name of the parameter that represents the name of the
  # fish

def find_two_word_fish(list_of_fish, start=0, two_word_fish=[]):
    if start == len(list_of_fish):
        return two_word_fish
    if len(list_of_fish[start].split()) == 2:
        two_word_fish.append(list_of_fish[start])
    return find_two_word_fish(list_of_fish, start + 1, two_word_fish)

two_word_fish_list = find_two_word_fish(list_of_fish)

for i, item in enumerate(list_of_fish):
    print(f'Fish name {i}: {item}')

print(f'The fish with the most word is: {max_fish}')
print(f'Fish names with two words: {two_word_fish_list}')

