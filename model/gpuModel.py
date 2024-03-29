import GPUtil
import cpuinfo

from psutil import virtual_memory, cpu_freq, cpu_count, cpu_percent
from time import sleep

def Mhz_to_Ghz(value):
    return f'{value/1000: .2f} Hz'

def bytes_to_gigas(value):
    return f'{value/1024/1024/1024: .1f} Gb'

def mega_to_giga(value):
    return f'{value/1024: .1f} Gb'

def memGpuPercent(total, using):
    return f'{(using*100)/total: .1f} %'

def dec_to_percent(value):
    return f'{value*100: .1f} %'

cont = 0


def show():
    gpu = GPUtil.getGPUs()[0] #atribui os dados da gpu
    cpu = cpuinfo.get_cpu_info()

    print('Total de memora ram: ', bytes_to_gigas(virtual_memory().total))
    print('Uso de memoria ram: ', bytes_to_gigas(virtual_memory().used))
    print('Uso de memoria ram: ', virtual_memory().percent, '% \n')

    print(cpu['brand_raw'])
    #print(cpu['hz_actual_friendly']) # key de frequencia usando cpuinfo
    #print(cpu['hz_advertised_friendly'])
    print('Frequancia base do cpu: ', Mhz_to_Ghz(cpu_freq().current))
    print('Quantidade de nucleos do cpu: ', cpu_count())
    print('Uso do cpu: ', cpu_percent(), '% \n') #para melhor precisao chamar em 0.1 s ou menor

    print(gpu.name)
    print('Temperatura da gpu: ', gpu.temperature, '°C') #Alt + 0176
    print('Memoria de gpu total: ', mega_to_giga(gpu.memoryTotal))
    print('Uso de memoria gpu: ', mega_to_giga(gpu.memoryUsed))
    print('Percentual da memoria gpu em uso: ', memGpuPercent(gpu.memoryTotal, gpu.memoryUsed))
    print('Percentual de uso gpu', dec_to_percent(gpu.load))

    print()
    #sleep(1)
