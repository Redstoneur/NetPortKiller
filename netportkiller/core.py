import psutil
import socket

def get_used_ports():
    ports_info = []
    for conn in psutil.net_connections(kind='inet'):
        if not conn.laddr or conn.status != psutil.CONN_LISTEN:
            continue

        port = conn.laddr.port
        pid = conn.pid
        proto = 'TCP' if conn.type == socket.SOCK_STREAM else 'UDP'

        if pid is None:
            continue

        try:
            proc = psutil.Process(pid)
            pname = proc.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pname = "Unknown"

        ports_info.append({
            'port': port,
            'protocol': proto,
            'pid': pid,
            'process': pname
        })
    return ports_info

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(3)
        return True
    except Exception:
        return False
