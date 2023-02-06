import sys
import re
import subprocess

def print_help():
    print("""
    Uso: python script.py [opciones]
    Opciones:
      -h, --help        Muestra esta ayuda
      -i, --ip          Dirección IP
    """)

def detect_os(ip):
    ttl = int(subprocess.check_output(["ping", "-c", "1", "-t", "1", ip]).decode("utf-8").split("ttl=")[1].split(" ")[0])

    if ttl >= 0 and ttl <= 64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    elif ttl >= 253 and ttl <= 255:
        return "Solaris"
    elif ttl >= 245 and ttl <= 247:
        return "FreeBSD"
    else:
        return "Sistema operativo no identificado"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    ip = None
    for i, arg in enumerate(sys.argv):
        if arg in ["-h", "--help"]:
            print_help()
            sys.exit(0)
        elif arg in ["-i", "--ip"]:
            if i + 1 < len(sys.argv):
                ip = sys.argv[i + 1]
            else:
                print("Falta especificar la dirección IP")
                print_help()
                sys.exit(1)

    if ip is None:
        print("Falta especificar la dirección IP")
        print_help()
        sys.exit(1)

    try:
        os = detect_os(ip)
        print("Sistema operativo detectado:", os)
    except subprocess.CalledProcessError as e:
        print("Comando inválido:", e)
        print_help()
        sys.exit(1)
