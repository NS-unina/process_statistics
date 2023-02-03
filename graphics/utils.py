import csv
from datetime import datetime

from statistics import mean



def times_to_millis(arr): 
    """Convert an array of timestamps into an array of seconds, starting from 0

    Args:
        arr (float): array of timestamps. 
    """
    start = arr[0]
    ret = []
    for i in arr: 
        ret.append(i - start)    

    return ret

def times_to_secs(arr):
    return [ t / 1000 for t in times_to_millis(arr) ]


class Stat:
    def __init__(self, timestamp, pid, virt, res, cpu, mem, command): 
        self.timestamp = timestamp
        self.interval_secs  = 0
        self.interval_millis = 0
        self.pid = pid 
        self.virt = virt 
        self.res = res 
        self.cpu = float(cpu.replace(",", "."))
        self.mem = float(mem.replace(",", "."))
        self.command = command

    def __str__(self):
        return f"{self.interval_secs},{self.pid},{self.virt},{self.res},{self.cpu},{self.mem},{self.command}"

    def get_for_matplotlib(stats, attr):
        """Returns two arrays, usable for matplotlib

        Args:
            stats (Array of Stat): The array of stats
            attr (string): the attribute name

        Returns:
             A dictionary in the form {x : [x], y : [y] }
        """
        secs = [s.interval_secs for s in stats]
        vals = [getattr(s, attr) for s in stats]
        return {
            'x' : secs, 
            'y' : vals
        }

    def get_average(stats, attr):
        vals = [getattr(s, attr) for s in stats]
        return mean(vals)




    def read_csv(csvname):
        stats = []
        print(f"[+] Process {csvname} file")
        with open(csvname) as csv_file: 
            csv_reader = csv.reader(csv_file, delimiter = ',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0: 
                    line_count += 1
                else:
                    s = Stat(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    stats.append(s)
                    line_count += 1


        print(f"[+] Processed {line_count} lines.")
        timestamps = [float(s.timestamp) for s in stats]
        t_millis    = times_to_millis(timestamps)
        t_secs      = times_to_secs(timestamps)
        for i in range(len(timestamps)):
            stats[i].interval_secs = t_secs[i]
            stats[i].interval_millis = t_millis[i]

        return stats






