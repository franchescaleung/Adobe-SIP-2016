import random
food = ["chicken", "beef", "shrimp", "crab", "pork", "pork chops", "fish", "eggs", "vegetables", "noodles"]
cooking_style = ["teriyaki ", "japanese ", "szechuan ",  "indian-style ", "vegetarian ", "steamed ", "fried ", "asian ", "homestyle ", "american style "]
adjective= ["spicy ", "crunchy ", "yummy ", "hot ", "cold ", "seasoned ", "chopped ", "fully-cooked ", "grilled ", "sauteed "]



counter=["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. ", "11. ", "12. ", "13. ", "14. ", "15. ", "16. ", "17. ", "18. ", "19. ", "20. "]

food_length = len(food)
cooking_style_length= len(cooking_style)
random_adjective_length= len(adjective)

    
def food_numbers():
    for i in range(10):
        random_food= random.randint(0, food_length-1)
        random_cooking_style= random.randint(0, cooking_style_length-1)
        random_adjective= random.randint(0, random_adjective_length-1)

        print(counter[i] + adjective [random_adjective ]  + cooking_style [random_cooking_style ] + food [random_food ])
        
food_numbers()

Article= ["The ", "A "]
Adjective= ["Rolling ", "Spinning ", "Jumping ", "Discoing "]
Name= ["Beans ", "Jettis ","Cups ", "Dolls "]


def bands():
    for i in range(20):
        random_art= random.randint(0, 1)
        random_adj= random.randint(0, 3)
        random_name= random.randint(0, 3)

        print(counter[i] + Article[random_art] + Adjective[random_adj] + Name[random_name])

bands
peint abs(-1)
