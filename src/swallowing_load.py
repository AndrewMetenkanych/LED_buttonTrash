import psutil
import GPUtil
import requests

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_gpu_load_and_temp():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu = gpus[0]  # Якщо кілька GPU, береться перший
        return gpu.load * 100, gpu.temperature
    else:
        return None, None  # Якщо GPU немає

def main():
    cpu_usage = get_cpu_usage()
    ram_usage = get_ram_usage()
    gpu_load, gpu_temp = get_gpu_load_and_temp()

    data = {
        'cpu_usage': cpu_usage,
        'ram_usage': ram_usage,
        'gpu_load': gpu_load,
        'gpu_temp': gpu_temp
    }
# Sending data on ESP32
    response = requests.post("http://<ESP32_IP_ADDRESS>/update", json=data)
    print(response.status_code)

if __name__ == "__main__":
    main()
