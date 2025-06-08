import socket
from enum import Enum
from typing import List, Optional, TypedDict

import psutil


class Protocol(str, Enum):
    TCP = "TCP"
    UDP = "UDP"


class PortInfo(TypedDict):
    port: int
    protocol: Protocol
    pid: int
    process: str


def get_used_ports() -> List[PortInfo]:
    """
    Récupère la liste des ports réseau actuellement utilisés en mode écoute (LISTEN).

    Parcourt toutes les connexions réseau de type 'inet' (IPv4/IPv6) et collecte les informations
    sur les ports en écoute, le protocole (TCP/UDP), le PID du processus associé et le nom du
    processus.

    :return: Liste de dictionnaires contenant les informations sur les ports utilisés.
    """
    ports_info: List[PortInfo] = []
    for conn in psutil.net_connections(kind='inet'):
        if not conn.laddr or conn.status != psutil.CONN_LISTEN:
            continue

        port: int = conn.laddr.port
        pid: Optional[int] = conn.pid
        proto: Protocol = Protocol.TCP if conn.type == socket.SOCK_STREAM else Protocol.UDP

        if pid is None:
            continue

        try:
            proc = psutil.Process(pid)
            pname: str = proc.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pname = "Unknown"

        ports_info.append({
            'port': port,
            'protocol': proto,
            'pid': pid,
            'process': pname
        })
    return ports_info


def kill_process(pid: int) -> bool:
    """
    Termine le processus correspondant au PID donné.

    Tente d'arrêter proprement le processus identifié par le PID fourni.
    Attend jusqu'à 3 secondes pour la terminaison du processus.

    :param pid: Identifiant du processus à terminer.
    :return: True si le processus a été terminé avec succès, False sinon.
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(3)
        return True
    except Exception:
        return False
