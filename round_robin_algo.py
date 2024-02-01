def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    rem_burst_time = list(burst_time)
    t = 0  # Current time

    while True:
        done = True

        for i in range(n):
            if rem_burst_time[i] > 0:
                done = False
                if rem_burst_time[i] > time_quantum:
                    t += time_quantum
                    rem_burst_time[i] -= time_quantum
                else:
                    t += rem_burst_time[i]
                    rem_burst_time[i] = 0
                    print(f"Process {processes[i]} finishes at time {t}")

        if done:
            break

# Example usage
processes = [1, 2, 3]
burst_time = [10, 5, 8]
time_quantum = 2

round_robin(processes, burst_time, time_quantum)
