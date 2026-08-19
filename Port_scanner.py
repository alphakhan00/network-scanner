import socket


print("***************** WELCOME TO NETWORK SCANNER *****************")

while True:
    target = input("Enter target IP or hostname: ")

    if target:
        break

    print("Target cannot be empty.")


print("\n1. Scan specific ports")
print("2. Scan all ports")

while True:
    choice = input("Choose an option: ")

    if choice == "1":
        scanning_port = input("Enter the ports you want to scan: ")
        ports = scanning_port.split(",")
        break

    elif choice == "2":
        ports = range(1, 65536)
        break

    else:
        print("Invalid option. Choose 1 or 2.")


results = {}


for i in ports:
    try:
        i = int(i)

        if 1 <= i <= 65535:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            try:
                result = s.connect_ex((target, i))

                if result == 0:
                    results[i] = "OPEN"
                else:
                    results[i] = "CLOSED"

            except socket.error:
                continue

            finally:
                s.close()

        else:
            print(i, "is an invalid port")
            continue

    except ValueError:
        print("Invalid port:", i)


print("\n&&&&&&&&&&& SCAN RESULTS &&&&&&&&&")

open_ports = 0
closed_ports = 0

for port, status in results.items():

    print("Port", port, "→", status)

    if status == "OPEN":
        open_ports += 1
    else:
        closed_ports += 1


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Total ports scanned:", len(results))
print("Open ports:", open_ports)
print("Closed ports:", closed_ports)


with open("scan_results.txt", "w") as file:
    file.write(f"The result of your target: {target}\n\n")

    for port, status in results.items():
        file.write(f"Port {port} → {status}\n")

    file.write("\n")
    file.write(f"Total ports scanned: {len(results)}\n")
    file.write(f"Open ports: {open_ports}\n")
    file.write(f"Closed ports: {closed_ports}\n")