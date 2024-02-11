sandwich_maker = {
    "Wholemeal": 1.00,
    "White": 0.80,
    "Cheesy white": 1.20,
    "Gluten Free": 1.40,
    "Chicken": 2.69,
    "Beef": 3.00,
    "Salami": 4.00,
    "Vegan slice": 3.30,
    "Onion": 1.69,
    "Tomato": 1.00,
    "Lettuce": 2.00,
    "Cheese": 2.50
}

def make_sandwich(bread, meat, lettuce):
    total_cost = sandwich_maker.get(bread, 0) + sandwich_maker.get(meat, 0) + sandwich_maker.get(lettuce, 0)
    return total_cost

def main():
    bread_choice = input("Select your bread (Wholemeal, White, Cheesy white, Gluten Free): ")
    meat_choice = input("Select your meat (Chicken, Beef, Salami, Vegan slice): ")
    lettuce_choice = input("Do you want lettuce? (Yes/No): ")

    if lettuce_choice.lower() == "yes":
        lettuce_choice = "Lettuce"
    else:
        lettuce_choice = ""

    total_cost = make_sandwich(bread_choice, meat_choice, lettuce_choice)
    if total_cost > 0:
        print("Your sandwich costs: ${:.2f}".format(total_cost))
    else:
        print("Sorry, we don't have the ingredients you selected.")

if __name__ == "__main__":
    main()

