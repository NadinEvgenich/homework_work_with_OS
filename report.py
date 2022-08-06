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
    return ", ".join({i.USER for i in get_processes()})


def get_process():
    return len(get_processes())


def get_user_process():
    up = Counter(i.USER for i in get_processes())
    return "\n\t".join([f"{key}: {value}" for key, value in up.items()])


def get_mem():
    lis1 = sum([int(i.RSS) for i in get_processes()])
    return round(lis1 / 10 ** 6, 2)


def get_cpu():
    return round(sum([float(i.CPU) for i in get_processes()]), 2)


def get_max_mem():
    m = max(get_processes(), key=lambda one_process: one_process.MEM)
    return f"{m.COMMAND[:20]} {m.MEM}%"


def get_max_cpu():
    c = max(get_processes(), key=lambda process: process.CPU)
    return f"{c.COMMAND[:20]} {c.MEM}%"


if __name__ == "__main__":
    print(f"Пользователи системы: {get_user()}")
    print(f"Процессов запущено: {get_process()}")
    print(f"Пользовательских процессов:\n\t{get_user_process()}")
    print(f"Всего памяти используется: {get_mem()} mb")
    print(f"Всего CPU используется: {get_cpu()} %")
    print(f"Больше всего памяти использует: {get_max_mem()} ")
    print(f"Больше всего CPU использует: {get_max_cpu()} ")
