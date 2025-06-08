"""
Module principal pour la gestion des ports réseau et des processus associés.
Fournit les fonctions pour lister les ports utilisés et tuer les processus par PID.
"""

import socket
from enum import Enum
from typing import List, Optional, TypedDict

import psutil


class Protocol(str, Enum):
    """
    Enumeration representing supported network protocols.
    - TCP: Transmission Control Protocol
    - UDP: User Datagram Protocol
    """
    TCP = "TCP"
    UDP = "UDP"


class PortInfo(TypedDict):
    """
    Dictionary-typed structure describing information about a used network port.
    - port: port number
    - protocol: network protocol (TCP or UDP)
    - pid: process ID using the port
    - process: name of the process using the port
    """
    port: int
    protocol: Protocol
    pid: int
    process: str


def get_used_ports() -> List[PortInfo]:
    """
    Retrieve the list of currently used network ports in listening mode (LISTEN).

    Iterates through all network connections of type 'inet' (IPv4/IPv6) and collects information
    about listening ports, protocol (TCP/UDP), associated process PID, and process name.

    :return: List of dictionaries containing information about used ports.
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
    Terminate the process corresponding to the given PID.

    Attempts to gracefully stop the process identified by the provided PID.
    Waits up to three seconds for the process to terminate.

    :param pid: Process ID to terminate.
    :return: True if the process was successfully terminated, False otherwise.
    """
    try:
        proc = psutil.Process(pid)
        proc.terminate()
        proc.wait(3)
        return True
    except psutil.Error:
        return False
