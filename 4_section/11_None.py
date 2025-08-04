shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "milk"
found_at = None
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)


print("found at position: {}".format(
    found_at if found_at is not None else "not found"))
