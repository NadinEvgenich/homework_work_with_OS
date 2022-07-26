import subprocess
from collections import namedtuple
from collections import Counter


def get_processes():
    output = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE, text=True).stdout.readlines()
    headers = [h for h in output[0].replace("%", "").strip().split() if h]
    Proc = namedtuple("Proc", headers)
    raw_data = map(lambda s: Proc(*s.strip().split(None, len(headers) - 1)), output[1:])
    return list(raw_data)


def get_user():
    return {i.USER for i in get_processes()}


def get_process():
    return len(get_processes())


def get_user_process():
    up = Counter(i.USER for i in get_processes())
    return up


def get_mem():
    lis1 = sum([int(i.RSS) for i in get_processes()])
    return lis1 / 10 ** 6


def get_cpu():
    return sum([float(i.CPU) for i in get_processes()])


def get_max_mem():
    return max([float(i.MEM) for i in get_processes()])

def get_max_cpu():
    return max([float(i.CPU) for i in get_processes()])



if __name__ == "__main__":
    print(f"Пользователи системы: {get_user()}")
    print(f"Процессов запущено: {get_process()}")
    print(f"Пользовательских процессов: {get_user_process()}")
    print(f"Всего памяти используется: {get_mem()} mb")
    print(f"Всего CPU используется: {get_cpu()} %")
    print(f"Больше всего памяти использует: {get_max_mem()} %")
    print(f"Больше всего CPU использует: {get_max_cpu()} %")
