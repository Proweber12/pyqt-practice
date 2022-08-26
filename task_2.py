from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping(text_previous_functions=True):
    while True:
        start_ip = input('Введите первоначальный адрес: ')
        try:
            last_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        end_ip = input('Сколько адресов проверить?: ')
        if end_ip.isnumeric():
            if (last_oct+int(end_ip)) > 254:
                print(f"Можем менять только последний октет, т.е. "
                        f"максимальное число хостов для проверки: {254-last_oct}")
            else:
                break
        else:
            print('Введите число')
            continue

    host_list = []
    for x in range(int(end_ip)):
        host_list.append(str(ip_address(start_ip)+x))
    return host_ping(host_list, text_previous_functions)


if __name__ == "__main__":
    host_range_ping()
