import config
# Запуск, эндпоинты

data_base = {}

while True:
    link = input('\nInput your link: ')
    data_base [config.keygen.key_generator()] = link
    print (data_base)