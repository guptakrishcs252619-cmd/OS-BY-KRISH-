from collections import deque

def round_robin(processes, quantum):
    n = len(processes)
    remaining = [p[2] for p in processes]
    completion = [0] * n
    response = [-1] * n
    time = 0
    context_switches = 0
    queue = deque(range(n))
    gantt = []

    while queue:
        i = queue.popleft()

        if response[i] == -1:
            response[i] = time - processes[i][1]

        run_time = min(quantum, remaining[i])

        gantt.append(processes[i][0])
        time += run_time
        remaining[i] -= run_time

        if remaining[i] > 0:
            queue.append(i)
            context_switches += 1
        else:
            completion[i] = time

        # Add processes that have arrived
        for j in range(n):
            if (processes[j][1] <= time and
                remaining[j] > 0 and
                j not in queue and
                j != i):
                queue.append(j)

    print("\nROUND ROBIN SCHEDULING")
    print("-" * 65)
    print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")

    total_tat = 0
    total_rt = 0

    for i, p in enumerate(processes):
        at = p[1]
        bt = p[2]
        tat = completion[i] - at
        wt = tat - bt
        rt = response[i]

        total_tat += tat
        total_rt += rt

        print(f"{p[0]}\t{at}\t{bt}\t{completion[i]}"
              f"\t{tat}\t{wt}\t{rt}")

    print("\nGantt Chart:")
    print(" -> ".join(gantt))

    print("\nAverage Turnaround Time:",
          round(total_tat / n, 2))
    print("Average Response Time:",
          round(total_rt / n, 2))
    print("Context Switches:", context_switches)


def fcfs(processes):
    time = 0
    total_tat = 0
    total_rt = 0
    context_switches = 0

    print("\nFCFS SCHEDULING")
    print("-" * 65)
    print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")

    gantt = []

    for i, p in enumerate(processes):
        name, at, bt = p

        if time < at:
            time = at

        response = time - at
        completion = time + bt
        turnaround = completion - at
        waiting = turnaround - bt

        total_tat += turnaround
        total_rt += response

        if gantt:
            context_switches += 1

        gantt.append(name)
        time = completion

        print(f"{name}\t{at}\t{bt}\t{completion}"
              f"\t{turnaround}\t{waiting}\t{response}")

    n = len(processes)

    print("\nGantt Chart:")
    print(" -> ".join(gantt))

    print("\nAverage Turnaround Time:",
          round(total_tat / n, 2))
    print("Average Response Time:",
          round(total_rt / n, 2))
    print("Context Switches:", context_switches)


# Process = (Process Name, Arrival Time, Burst Time)
processes = [
    ("P1", 0, 8),
    ("P2", 1, 4),
    ("P3", 2, 9),
    ("P4", 3, 5)
]

quantum = int(input("Enter Time Quantum: "))

round_robin(processes, quantum)
fcfs(processes)
print("krish 085")
