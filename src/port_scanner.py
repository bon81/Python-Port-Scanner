import sys
import socket
import logging
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(
    filename="scan_results.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def scan_port(target, port):
    """Scans a single port on the target."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                service = (
                    socket.getservbyport(port, "tcp")
                    if port <= 1023
                    else "Unknown Service"
                )
                msg = f"Port {port} is open ({service})"
                print(msg)
                logging.info(msg)
    except Exception as e:
        logging.error(f"Error scanning port {port}: {e}")


def port_scanner(target, ports):
    """Scans multiple ports using multi-threading."""
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda p: scan_port(target, p), ports)


if __name__ == "__main__":
    # Ensure a target is provided
    if len(sys.argv) != 2:
        print("Usage: python <filename> <hostname/IP>")
        sys.exit(1)

    # Convert hostname to IPv4
    try:
        target = socket.gethostbyname(sys.argv[1])
    except socket.gaierror:
        print("Error: Invalid hostname. Please enter a valid IP or domain.")
        sys.exit(1)

    # Display scan details
    print("=" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scan Started at: {datetime.now()}")
    print("=" * 50)

    logging.info(f"Scanning started for {target} at {datetime.now()}")

    try:
        port_scanner(target, range(1, 1024))
    except KeyboardInterrupt:
        print("\nScan halted by user.")
        logging.warning("Scan halted by user.")
        sys.exit(1)
    except socket.timeout:
        print("\nError: Connection timed out. The target may be unreachable.")
        logging.error("Connection timed out. The target may be unreachable.")
        sys.exit(1)

    print("=" * 50)
    print("Scan complete! Results saved to scan_results.log")
    logging.info("Scan complete!")
