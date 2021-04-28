# File System is that we have to use recursive algorithm for computing disk usage.
# OS Module is used here to acheive this task.
print()

import os

def disk_usage(path):
    total_size=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            t_s=disk_usage(childpath)
            if t_s is None:
                continue
            else:
                total_size=total_size+t_s
    print(total_size)


path="E:\\PYTHON PROGRAMs"

disk_usage(path)