# Round Robin CPU Scheduling
# Time Quantum = 2 ms

processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 6]
]

quantum = 2

# Store remaining burst time
remaining = {}
arrival = {}
burst = {}
completion = {}

for p, at, bt in processes:
    remaining[p] = bt
    arrival[p] = at
    burst[p] = bt

queue = []
time = 0
completed = 0
added = set()
gantt = []

while completed < len(processes):

    # Add processes that have arrived
    for p, at, bt in processes:
        if at <= time and p not in added:
            queue.append(p)
            added.add(p)

    # If queue is empty, move time to next arrival
    if not queue:
        time += 1
        continue

    # Select first process
    p = queue.pop(0)

    start = time

    # Execute for quantum or remaining burst
    execution = min(quantum, remaining[p])
    time += execution
    remaining[p] -= execution

    gantt.append((p, start, time))

    # Add newly arrived processes
    for proc, at, bt in processes:
        if at <= time and proc not in added:
            queue.append(proc)
            added.add(proc)

    # If process is not completed, put it back
    if remaining[p] > 0:
        queue.append(p)
    else:
        completion[p] = time
        completed += 1


# -------------------------------
# Calculate TAT and WT
# -------------------------------

total_tat = 0
total_wt = 0

print("========== ROUND ROBIN ==========")
print("Time Quantum =", quantum, "ms")

print("\nGantt Chart:")
for p, start, end in gantt:
    print(f"| {p} {start}-{end} ", end="")
print("|")

print("\n")
print("Process\tAT\tBT\tCT\tTAT\tWT")

for p, at, bt in processes:

    ct = completion[p]

    # Turnaround Time
    tat = ct - at

    # Waiting Time
    wt = tat - bt

    total_tat += tat
    total_wt += wt

    print(f"{p}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")


# Average values
n = len(processes)

avg_tat = total_tat / n
avg_wt = total_wt / n

print("\nAverage Turnaround Time =", round(avg_tat, 2), "ms")
print("Average Waiting Time =", round(avg_wt, 2), "ms")
PRINT("KRISH 085")
