import psutil, platform, os

def get_os():
    return platform.platform()

def get_PID():
    return os.getpid()

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    ram = psutil.virtual_memory()

    # conversão de bytes para mb
    return ram.used / (1024 * 1024)

def get_names():
    return ["André Esteves Arantes", "Fernando Aschwanden", "Gustavo Jansen"]
