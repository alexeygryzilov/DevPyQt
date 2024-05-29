import time
from platform import uname
import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, delay=None, parent=None):
        super().__init__(parent)

        self.delay = delay
        self.status = True

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while self.status:
            processor = uname().processor
            cores = psutil.cpu_count(logical=False)
            cpu_value = psutil.cpu_percent()
            ram_total = psutil.virtual_memory().total
            ram_value = psutil.virtual_memory().percent
            disks_number = len(psutil.disk_partitions())
            disk_partitions = psutil.disk_partitions(all=False)
            disks = [disk_partitions[idx][0] for idx in range(disks_number)]
            processes = [p.name() for p in psutil.process_iter()]
            services = [s.name() for s in psutil.win_service_iter()]
            self.systemInfoReceived.emit([processor, cores, cpu_value, ram_total, ram_value,
                                          disks_number, disk_partitions, processes, services, disks])
            self.sleep(self.delay)

