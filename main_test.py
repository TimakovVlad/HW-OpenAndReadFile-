
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_dict = {}
    for item in dishes:
        list_ing = cook_book[item]
        print(list_ing)
        for i in range(len(list_ing)):
            list_temp = list(list_ing[i].values())
            print(list_temp)
            dict_temp = {}
            dict_temp['measure'] = list_temp[2]
            if list_temp[0] in shop_list_dict:
                dict_temp['quantity'] = list_temp[1] * person_count
                temp_2 = shop_list_dict[list_temp[0]]
                dict_temp['quantity'] += temp_2['quantity']
                shop_list_dict[list_temp[0]] = dict_temp
            else:
                dict_temp['quantity'] = list_temp[1] * person_count
                shop_list_dict[list_temp[0]] = dict_temp
    return shop_list_dict


print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))