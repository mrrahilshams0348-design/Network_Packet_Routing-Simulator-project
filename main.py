from controller import run_cpp_routing
from visualize import animate_routing

def extract_path(output):
    for line in output.splitlines():
        if line.startswith("Path:"):
            nums = line.replace("Path:", "").strip().split()
            return [int(x) for x in nums]
    return []

def main():
    print("=== Network Packet Routing Simulator ===")

    src = int(input("Enter source node (0-4): "))
    dst = int(input("Enter destination node (0-4): "))

    output = run_cpp_routing(src, dst)
    print(output)

    path = extract_path(output)

    if not path:
        print("Error extracting path")
        return

    animate_routing(path)

if __name__ == "__main__":
    main()
