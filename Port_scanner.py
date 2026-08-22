import socket


def get_target():
    while True:
        target = input("Enter target IP or hostname: ").strip()

        if target:
            return target

        print("Target cannot be empty.")


def get_ports():
    print("\n1. Scan specific ports")
    print("2. Scan all ports")

    while True:
        choice = input("Choose an option: ").strip()

        if choice == "1":
            port_input = input("Enter the ports you want to scan: ")
            return port_input.split(",")

        elif choice == "2":
            return range(1, 65536)

        else:
            print("Invalid option. Choose 1 or 2.")


def scan_port(target, port):
    try:
        port = int(port)

        if not 1 <= port <= 65535:
            print(f"{port} is an invalid port.")
            return None

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(0.5)
            result = scanner.connect_ex((target, port))

            if result == 0:
                return "OPEN"

            return "CLOSED"

    except ValueError:
        print(f"Invalid port: {port}")
        return None

    except socket.gaierror:
        print("Unable to resolve the target.")
        return None

    except socket.error as error:
        print(f"Socket error on port {port}: {error}")
        return None


def display_results(target, results):
    print("\n" + "=" * 45)
    print("              SCAN RESULTS")
    print("=" * 45)

    open_ports = 0
    closed_ports = 0

    for port, status in results.items():
        print(f"Port {port:<5} → {status}")

        if status == "OPEN":
            open_ports += 1
        else:
            closed_ports += 1

    print("=" * 45)
    print(f"Total ports scanned: {len(results)}")
    print(f"Open ports: {open_ports}")
    print(f"Closed ports: {closed_ports}")
    print("=" * 45)


def save_results(target, results):
    open_ports = sum(1 for status in results.values() if status == "OPEN")
    closed_ports = sum(1 for status in results.values() if status == "CLOSED")

    with open("scan_results.txt", "w") as file:
        file.write(f"Scan target: {target}\n\n")

        for port, status in results.items():
            file.write(f"Port {port} → {status}\n")

        file.write("\n")
        file.write(f"Total ports scanned: {len(results)}\n")
        file.write(f"Open ports: {open_ports}\n")
        file.write(f"Closed ports: {closed_ports}\n")


def main():
    print("=" * 60)
    print("             WELCOME TO NETWORK SCANNER")
    print("=" * 60)

    target = get_target()
    ports = get_ports()

    results = {}

    print("\nStarting scan...\n")

    for port in ports:
        status = scan_port(target, port)

        if status is not None:
            try:
                port_number = int(port)
                results[port_number] = status
            except ValueError:
                continue

    display_results(target, results)
    save_results(target, results)

    print("\nResults saved to scan_results.txt")


if __name__ == "__main__":
    main()
