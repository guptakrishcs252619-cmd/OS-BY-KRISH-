# CPU Scheduling: Round Robin and FCFS

processes = [
    ("P1", 0, 5),
    ("P2", 4, 2),
    ("P3", 5, 4)
]

# --------------------------------------------------
# ROUND ROBIN
# --------------------------------------------------

def round_robin(processes, quantum):
    n = len(processes)
    remaining = {p[0]: p[2] for p in processes}
    arrival = {p[0]: p[1] for p in processes}
    burst = {p[0]: p[2] for p in processes}

    completed = {}
    queue = []
    gantt = []

    time = 0
    added = set()

    while len(completed) < n:

        # Add arrived processes
        for p, at, bt in processes:
            if at <= time and p not in added and p not in completed:
                queue.append(p)
                added.add(p)

        # CPU idle
        if not queue:
            future = [at for p, at, bt in processes
                      if p not in added and p not in completed]

            if future:
                time = min(future)
                continue

        p = queue.pop(0)

        start = time
        run = min(quantum, remaining[p])
        time += run
        remaining[p] -= run

        gantt.append((p, start, time))

        # Add newly arrived processes
        for proc, at, bt in processes:
            if at <= time and proc not in added and proc not in completed:
                queue.append(proc)
                added.add(proc)

        if remaining[p] > 0:
            queue.append(p)
        else:
            completed[p] = time

    print("\n========== ROUND ROBIN ==========")
    print("Time Quantum =", quantum, "ms")

    print("\nGantt Chart:")
    for p, start, end in gantt:
        print(f"| {p} ({start}-{end}) ", end="")
    print("|")

    total_tat = 0
    total_wt = 0

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

    for p, at, bt in processes:
        ct = completed[p]
        tat = ct - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        print(f"{p}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    print("\nAverage Turnaround Time =",
          round(total_tat / n, 2), "ms")

    print("Average Waiting Time =",
          round(total_wt / n, 2), "ms")


# --------------------------------------------------
# FCFS
# --------------------------------------------------

def fcfs(processes):

    # Sort according to arrival time
    processes = sorted(processes, key=lambda x: x[1])

    time = 0
    total_tat = 0
    total_wt = 0

    print("\n========== KRISH 085 FCFS ==========")

    print("\nGantt Chart:")

    completion = {}

    for p, at, bt in processes:

        if time < at:
            time = at

        start = time
        time += bt
        completion[p] = time

        print(f"| {p} ({start}-{time}) ", end="")

    print("|")

    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

    for p, at, bt in processes:

        ct = completion[p]
        tat = ct - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        print(f"{p}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    n = len(processes)

    print("\nAverage Turnaround Time =",
          round(total_tat / n, 2), "ms")

    print("Average Waiting Time =",
          round(total_wt / n, 2), "ms")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

round_robin(processes, 2)
fcfs(processes)
