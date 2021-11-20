from pprint import pprint

import os

path = os.path.join(os.getcwd(), 'Recipies.txt')

with open(path, encoding = 'utf-8') as f:
    # print(f.read())
    cook_book ={}
    for course in f:
        course_name = course.strip()
        counter = int(f.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = f.readline().split('|')
            temp_data.append(
                {'ingredient_name': ingredient_name.strip(),
                 'quantity': int(quantity.strip()), 'measure': measure.strip()}
            )
        cook_book[course_name] = temp_data
        f.readline()
    pprint(cook_book)

    print()

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for ingredient in cook_book[dish]:
                # print(ingredient)
                new_shopping_list = {ingredient['ingredient_name']:{'measure':ingredient['measure'],
                                                                     'quantity':ingredient['quantity']*person_count}}
                # print(new_shopping_list[ingredient['ingredient_name']])
                if shop_list.get(ingredient['ingredient_name']):
                    new_item = (int(shop_list[ingredient['ingredient_name']]['quantity']) +
                                  int(new_shopping_list[ingredient['ingredient_name']]['quantity']))
                    shop_list[ingredient['ingredient_name']]['quantity'] = new_item
                    # print(new_item)
                else:
                    shop_list.update(new_shopping_list)
        pprint(shop_list)


    get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3)









