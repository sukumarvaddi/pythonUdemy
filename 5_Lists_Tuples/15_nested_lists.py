menu = [["egg", "bacon"],
        ["egg", "sausage", "bacon"],
        ["egg", "spam"],
        ["egg", "bacon",  "spam"],
        ["egg", "bacon", "sausage", "spam"],
        ["spam", "bacon", "sausage", "spam"],
        ["spam", "egg", "spam", "spam", "bacon", "spam"],
        ["spam", "egg", "sausage", "spam"]]


# for menu_items in menu:
#     menu_items_length_index = len(menu_items)-1
#     for index, sub_item in enumerate(reversed(menu_items)):
#         if sub_item == "spam":
#             del (menu_items[menu_items_length_index-index])
#     print(menu_items)

for menu_items in menu:
    for index in range(len(menu_items)-1, -1, -1):
        if menu_items[index] == "spam":
            del (menu_items[index])
    print(menu_items)
