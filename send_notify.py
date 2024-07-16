import os

target_device_ip = "192.168.1.x"  # Replace with the IP address of the target device
os.system(f'ssh username@{target_device_ip} "python ~/notify.py"')
