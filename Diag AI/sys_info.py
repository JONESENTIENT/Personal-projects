import platform
import psutil
import cpuinfo
import GPUtil
import socket
import distutils

def run():

    # System Information

    system_info = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
    }



    # CPU Information

    detailed_cpu_info = cpuinfo.get_cpu_info()
    cpu_info = {
        "cores": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq()._asdict(),
        "usage": psutil.cpu_percent(interval=1, percpu=True)
    }



    # Battery info

    battery = psutil.sensors_battery()
    if battery is not None:
        if hasattr(psutil, "sensors_battery"):
            battery = psutil.sensors_battery()
            battery_info = {
                "percent": battery.percent,
                "plugged": battery.power_plugged,
                "secs_left": battery.secsleft,
            }

    else:
        battery_info = "No battery information available."



    # Memory Information

    memory_info = psutil.virtual_memory()._asdict()



    # Disk Information

    disk_info = [disk._asdict() for disk in psutil.disk_partitions()]
    disk_usage = [psutil.disk_usage(disk.mountpoint)._asdict() for disk in psutil.disk_partitions()]



    # Network Information

    network_info1 = psutil.net_if_addrs()
    network_stats = psutil.net_if_stats()



    # GPU Information

    gpus = []
    for gpu in GPUtil.getGPUs():
        gpu_info = {
            "id": gpu.id,
            "name": gpu.name,
            "load": gpu.load,
            "temperature": gpu.temperature,
            "memoryFree": gpu.memoryFree,
            "memoryUsed": gpu.memoryUsed,
            "driver": gpu.driver
        }
        gpus.append(gpu_info)
        


    #Check disk I?O

    disk_io_counters = psutil.disk_io_counters()._asdict()


    # Network Hostname and IP

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    network_info2 = {
        "hostname": hostname,
        "ip_address": ip_address,
        "network_interfaces": psutil.net_if_addrs()
    }

    print([system_info, detailed_cpu_info,cpu_info,battery_info, memory_info, disk_info, disk_usage, network_info1, network_stats, gpus, disk_io_counters, network_info2])

run()