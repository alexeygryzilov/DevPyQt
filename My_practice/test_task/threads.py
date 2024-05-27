import time
from platform import uname
import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def run(self) -> None:
        if self.delay is None:
            self.delay = 1

        while True:
            processor = uname().processor
            cores = psutil.cpu_count(logical=False)
            cpu_value = psutil.cpu_percent()
            ram_total = psutil.virtual_memory().total
            ram_value = psutil.virtual_memory().percent
            disks_number = len(psutil.disk_partitions())
            disk_partitions = psutil.disk_partitions()
            self.systemInfoReceived.emit([processor, cores, cpu_value, ram_total, ram_value,
                                          disks_number, disk_partitions])
            time.sleep(self.delay)
