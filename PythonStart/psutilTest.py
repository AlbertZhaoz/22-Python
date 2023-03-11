import psutil

print(psutil.cpu_count())
print(psutil.cpu_times())
print(psutil.cpu_percent(interval=1, percpu=True))
print(psutil.virtual_memory())
print(psutil.test())