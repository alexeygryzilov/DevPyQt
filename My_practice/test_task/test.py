import psutil

data = psutil.disk_partitions()

disks = [data[idx][0] for idx in range(len(data))]
print(disks)

for disk in disks:
    disk_ = psutil.disk_usage(disk)
    print(f'{disk} total= {disk_[0]} used= {disk_[1]} free= {disk_[2]} percent= {disk_[3]}')