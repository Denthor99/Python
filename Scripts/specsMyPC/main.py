import psutil
import GPUtil


# Hercios de una CPU
def obtener_info_cpu():
    cpu_info = psutil.cpu_freq()
    return f'Frecuencia de la CPU: {cpu_info.current:.2f} MHz'


# Memoria RAM total del equipo
def obtener_memoria_total():
    memory_info = psutil.virtual_memory()
    return f'Memoria total: {memory_info.total // (1024 ** 3):.2f} GB'


# Memoria RAM usada actualmente
def obtener_memoria_usada():
    memory_info = psutil.virtual_memory()
    return f'Memoria usada: {memory_info.used // (1024 ** 3):.2f} GB'


# Discos duros y su espacio libre
def obtener_discos():
    disk_info = psutil.disk_partitions(all=True)
    disks = []
    for disk in disk_info:
        if disk.fstype != '':
            free_space = psutil.disk_usage(disk.mountpoint).free // (1024 ** 3)
            disks.append(f'{disk.device}: {disk.fstype}, Espacio libre: {free_space:.2f} GB')
    return '\n'.join(disks)


# Información sobre todas las GPUs disponibles
def obtener_info_gpus():
    gpus = GPUtil.getGPUs()
    if not gpus:
        return "No se ha encontrado una tarjeta gráfica."

    info_gpus = []
    for gpu in gpus:
        info_gpus.append(
            f"GPU ID: {gpu.id}\n"
            f"Versión del driver (NVIDIA): {gpu.driver}\n"
            f"Memoria VRAM total: {gpu.memoryTotal / 1024:.2f} GB\n"
            f"Memoria VRAM usada: {gpu.memoryUsed / 1024:.2f} GB\n"
            f"Porcentaje de utilización: {gpu.load * 100:.2f}%\n"
            f"Nombre de la tarjeta gráfica: {gpu.name}\n"
            f"Temperatura actual: {gpu.temperature}°C\n"
        )

    return "\n".join(info_gpus)


if __name__ == '__main__':
    print(obtener_info_cpu())
    print(obtener_memoria_total())
    print(obtener_memoria_usada())
    print(obtener_discos())
    print(obtener_info_gpus())
