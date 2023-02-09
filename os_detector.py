import re
import sys
import subprocess

def main(ip):
    try:
        result = subprocess.check_output(["ping", "-c", "1", "-t", "1", ip])
        ttl = int(re.search(r"ttl=(\d+)", result.decode("utf-8")).group(1))
        if ttl >= 0 and ttl <= 64:
            print("Sistema operativo: Linux")
        elif ttl >= 65 and ttl <= 128:
            print("Sistema operativo: Windows")
        elif ttl >= 245 and ttl <= 247:
            print("Sistema operativo: FreeBSD")
        elif ttl >= 253 and ttl <= 255:
            print("Sistema operativo: Solaris")
        else:
            print("Sistema operativo no identificado")
    except subprocess.CalledProcessError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python os_detector.py direccion_ip")
        sys.exit(1)
    ip = sys.argv[1]
    main(ip)
