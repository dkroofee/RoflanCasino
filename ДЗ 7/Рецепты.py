ingredient_hold_mn = set()
ingredient_eat = set()
ingredient_hold = int(input())
for i in range(ingredient_hold):
    ingredient_hold_mn.add(input())
name_recipe_N = int(input())
for i in range(name_recipe_N):
    name_recipe = input()
    ingredient_eat_M = int(input())
    flag = True
    for j in range(ingredient_eat_M):
        ingredient_eat.add(input())
    for i in ingredient_eat:
        if not i in ingredient_hold_mn:
            flag = False
    if flag:
        print(name_recipe)
    ingredient_eat = set()