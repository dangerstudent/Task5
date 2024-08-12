immutable_var = 1, 2, "srtring", "dustun", True
print(immutable_var)
immutable_var[4] = 180 #Здесь нам выдает ошибку потому что кортедж не поддерживает обращение по элементам
mutable_list = [1, 2, "string", "order", True]
mutable_list[4] = 12
print(mutable_list)