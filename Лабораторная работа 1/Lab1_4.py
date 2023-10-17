users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_ = {
    "Общее количество": "0",
    "Уникальные посещения": "0",
}
all_quant = len(users)
unic_quant = len(set(users))
dict_["Общее количество"] = all_quant
dict_["Уникальные посещения"] = unic_quant
print(dict_)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
