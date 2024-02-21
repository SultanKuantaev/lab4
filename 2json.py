import json
with open("sample-data.json", "r") as my_file:
    json_string = my_file.read()
data = json.loads(json_string)
def format_interface_data(data):
    # Получаем список интерфейсов
    interfaces = data.get('imdata', [])

    # Печатаем заголовок таблицы
    header = f"{'Interface Status':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}"
    print(header)
    print('-' * len(header))

    # Итерируем по каждому интерфейсу и печатаем информацию
    for interface in interfaces:
        attr = interface['l1PhysIf']['attributes']
        
        print(f"{attr['dn']:<50} {attr['descr']:<20} {attr['speed']:<8} {attr['mtu']:<6}")

# Вызываем функцию и передаем ей данные
format_interface_data(data)
