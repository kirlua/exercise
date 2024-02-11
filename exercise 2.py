list_of_fish = [
    "flounder", "sole", "blue cod", "snapper", "terakihi", "john dory",
    "red cod"
]

list_of_fish = [
    "flounder", "sole", "blue cod", "snapper", "terakihi", "john dory",
    "red cod"
]

def print_first_three_letters(list_of_fish, start=0, first_three_letters=[]):
    if start == len(list_of_fish):
        return first_three_letters
    first_three_letters.append(list_of_fish[start][:3])
    return print_first_three_letters(list_of_fish, start + 1, first_three_letters)

first_three_letters = print_first_three_letters(list_of_fish)
print("First three letters of each fish name:", first_three_letters)
