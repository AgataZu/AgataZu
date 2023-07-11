import psutil

# Get the current CPU usage
cpu_usage = psutil.cpu_percent()

# Get the current memory usage
memory_usage = psutil.virtual_memory().percent

# Get the current disk usage
disk_usage = psutil.disk_usage("/").percent

# Print the collected data
print(f"CPU usage: {cpu_usage}%")
print(f"Memory usage: {memory_usage}%")
print(f"Disk usage: {disk_usage}%")
