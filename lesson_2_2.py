import json

with open('cookbook.json') as f:
    cookbook = json.load(f)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cookbook[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['количество'] *= person_count
            if new_shop_list_item['название_ингредиента'] not in shop_list:
                shop_list[new_shop_list_item['название_ингредиента']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['название_ингредиента']]['количество'] += new_shop_list_item['количество']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['название_ингредиента'], shop_list_item['количество'],
                                shop_list_item['ед_измерения']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()