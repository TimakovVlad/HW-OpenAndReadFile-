def mini_dict(str_ing):
    dict_ = {}
    # print(str_ing)
    list_spl = str_ing.split(' | ')
    dict_['ingredient_name'] = list_spl[0]
    dict_['quantity'] = int(list_spl[1])
    if list_spl[2][-1] == '\n':
        dict_['measure'] = list_spl[2][:-1]
    else:
        dict_['measure'] = list_spl[2]
    return dict_


def cook_book_dict(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as f:
        all_file = f.readlines()
        i = 0
        while len(all_file) >= i:
            name_dish = all_file[i][:-1]
            cook_book[name_dish] = []
            len_ing = int(all_file[i+1])
            i += 2
            for j in range(len_ing):
                cook_book[name_dish].append(mini_dict(all_file[i+j]))
            i += (len_ing + 1)
    return cook_book


cook_book = cook_book_dict('cook_book.txt')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_dict = {}
    for item in dishes:
        list_ing = cook_book[item]
        for i in range(len(list_ing)):
            list_temp = list(list_ing[i].values())
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