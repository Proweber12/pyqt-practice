from tabulate import tabulate
from task_2 import host_range_ping


def host_range_ping_tab(text_previous_functions=True):
    res_dict = host_range_ping(text_previous_functions)
    print(tabulate([res_dict], headers='keys', tablefmt="grid", stralign="center"))


if __name__ == "__main__":
    host_range_ping_tab(False)
