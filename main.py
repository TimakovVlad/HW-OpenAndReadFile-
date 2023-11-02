def mini_dict(str_ing):
    dict_ = {}
    # print(str_ing)
    list_spl = str_ing.split(' | ')
    dict_['ingredient_name'] = list_spl[0]
    dict_['quantity'] = list_spl[1]
    dict_['measure'] = list_spl[2][:-1]
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



print(cook_book_dict('cook_book.txt'))