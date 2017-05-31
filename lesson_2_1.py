import json
def get_cookbook_from_file():
        with open('cookbook.txt', 'r') as cookbook:
                cookbook_copy = {}
                while True:
                        dish_name = cookbook.readline().lower().strip()
                        if dish_name:
                                cookbook_copy[dish_name] = []
                                count_of_ingridients = int(cookbook.readline())
                                for i in range(count_of_ingridients):
                                    ingridient = {}
                                    temp_ingridient = cookbook.readline().split(' | ')
                                    ingridient['название_ингредиента'] = temp_ingridient[0].strip()
                                    ingridient['количество'] = int(temp_ingridient[1].strip())
                                    ingridient['ед_измерения'] = temp_ingridient[2].strip()
                                    cookbook_copy[dish_name].append(ingridient)
                        else:
                            break
                return cookbook_copy

def create_cookbook_json():
    with open('cookbook.json', 'w') as cookbook_json:
        json.dump(get_cookbook_from_file(), cookbook_json, indent = 2, ensure_ascii = False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in get_cookbook_from_file()[dish]:
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