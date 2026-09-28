import random

print("085 - Krish Gupta")

requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200

def calculate_movement(order, head):
    movement = 0
    current = head
    for request in order:
        movement += abs(current - request)
        current = request
    return movement

def fcfs(requests, head):
    order = requests[:]
    return order, calculate_movement(order, head)

def sstf(requests, head):
    pending = requests[:]
    order = []
    current = head

    while pending:
        nearest = min(pending, key=lambda x: abs(x - current))
        order.append(nearest)
        pending.remove(nearest)
        current = nearest

    return order, calculate_movement(order, head)

def cscan(requests, head, disk_size):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    order = right + left
    movement = 0
    current = head

    for request in right:
        movement += abs(current - request)
        current = request

    if left:
        movement += abs(current - (disk_size - 1))
        movement += disk_size - 1
        current = 0

    for request in left:
        movement += abs(current - request)
        current = request

    return order, movement

def clook(requests, head):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    order = right + left

    return order, calculate_movement(order, head)

def rss(requests, head):
    order = requests[:]
    random.shuffle(order)

    return order, calculate_movement(order, head)

def disk_scheduling():
    while True:
        print("\nDisk Scheduling")
        print("1. FCFS")
        print("2. SSTF")
        print("3. C-SCAN")
        print("4. C-LOOK")
        print("5. RSS")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            order, movement = fcfs(requests, head)

        elif choice == "2":
            order, movement = sstf(requests, head)

        elif choice == "3":
            order, movement = cscan(requests, head, disk_size)

        elif choice == "4":
            order, movement = clook(requests, head)

        elif choice == "5":
            order, movement = rss(requests, head)

        elif choice == "6":
            break

        else:
            print("Invalid choice")
            continue

        print("Request Order:", order)
        print("Total Head Movement:", movement)


BLOCK_SIZE = 10
TOTAL_BLOCKS = 10

disk = [None] * TOTAL_BLOCKS
directory = {}

def create_file():
    name = input("Enter file name: ")

    if name in directory:
        print("File already exists")
        return

    content = input("Enter file content: ")

    required_blocks = (len(content) + BLOCK_SIZE - 1) // BLOCK_SIZE

    free_blocks = [i for i in range(TOTAL_BLOCKS) if disk[i] is None]

    if required_blocks > len(free_blocks):
        print("Not enough disk space")
        return

    allocated_blocks = free_blocks[:required_blocks]

    for i, block in enumerate(allocated_blocks):
        disk[block] = content[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]

    directory[name] = allocated_blocks

    print("File created successfully")

def read_file():
    name = input("Enter file name: ")

    if name not in directory:
        print("File not found")
        return

    content = ""

    for block in directory[name]:
        content += disk[block]

    print("File Content:", content)

def delete_file():
    name = input("Enter file name: ")

    if name not in directory:
        print("File not found")
        return

    for block in directory[name]:
        disk[block] = None

    del directory[name]

    print("File deleted successfully")

def show_directory():
    if not directory:
        print("Directory is empty")
        return

    print("\nDirectory")

    for name, blocks in directory.items():
        print(name, ":", blocks)

def show_disk():
    print("\nDisk Blocks")

    for i, block in enumerate(disk):
        print(i, ":", block)

def file_system():
    while True:
        print("\nSimple File System")
        print("1. Create File")
        print("2. Read File")
        print("3. Delete File")
        print("4. Show Directory")
        print("5. Show Disk Blocks")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            read_file()

        elif choice == "3":
            delete_file()

        elif choice == "4":
            show_directory()

        elif choice == "5":
            show_disk()

        elif choice == "6":
            break

        else:
            print("Invalid choice")


while True:
    print("\nMain Menu")
    print("1. Disk Scheduling")
    print("2. Simple File System")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        disk_scheduling()

    elif choice == "2":
        file_system()

    elif choice == "3":
        print("Program terminated")
        break

    else:
        print("Invalid choice")

