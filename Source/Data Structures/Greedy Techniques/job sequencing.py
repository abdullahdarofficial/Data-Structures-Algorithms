class Job:
    def __init__(self, id, deadline, profit):
        self.id = id  # Job ID
        self.deadline = deadline  # Job deadline
        self.profit = profit  # Profit associated with the job

def job_sequencing(jobs):
    """
    Schedules jobs to maximize total profit. A job can be completed by its deadline.

    :param jobs: List of Job objects
    :return: A tuple containing the list of scheduled job IDs and the total profit
    """
    # Step 1: Sort jobs according to decreasing profit
    # Time complexity: O(n log n), where n is the number of jobs, due to sorting
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Find the maximum deadline to determine the schedule size
    # Time complexity: O(n), where n is the number of jobs
    max_deadline = max(job.deadline for job in jobs)

    # Step 3: Initialize a schedule array to keep track of free slots, initialized with -1 (unassigned slots)
    # Time complexity: O(max_deadline), as we initialize the array with max_deadline slots
    schedule = [-1] * max_deadline
    total_profit = 0  # To track the total profit

    # Step 4: Iterate over the sorted jobs to schedule them
    # Time complexity: O(n * max_deadline), where n is the number of jobs and max_deadline is the number of slots
    for job in jobs:
        # Step 5: Find a free slot for this job, starting from the latest possible slot (min of job's deadline and max_deadline)
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            # If the slot is free, schedule the job
            if schedule[slot] == -1:
                schedule[slot] = job.id  # Assign job ID to this slot
                total_profit += job.profit  # Add the job's profit to total profit
                break  # Move to the next job once this one is scheduled

    # Step 6: Collect scheduled job IDs
    # Time complexity: O(max_deadline), as we iterate over the schedule array to gather the scheduled jobs
    scheduled_jobs = [j for j in schedule if j != -1]

    return scheduled_jobs, total_profit

# Example usage
jobs = [
    Job('A', 2, 100),  # Job A with deadline 2 and profit 100
    Job('B', 1, 19),   # Job B with deadline 1 and profit 19
    Job('C', 2, 27),   # Job C with deadline 2 and profit 27
    Job('D', 1, 25),   # Job D with deadline 1 and profit 25
    Job('E', 3, 15)    # Job E with deadline 3 and profit 15
]

# Schedule jobs to maximize profit
scheduled_jobs, total_profit = job_sequencing(jobs)

# Output the scheduled jobs and the total profit
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)

# -------------------------------
# Time complexity analysis:
# -------------------------------

# 1. Sorting jobs by profit:
#    - Time complexity: O(n log n), where n is the number of jobs, due to sorting the jobs based on profit.

# 2. Finding the maximum deadline:
#    - Time complexity: O(n), where n is the number of jobs, as we iterate over the jobs to find the maximum deadline.

# 3. Scheduling the jobs:
#    - Time complexity: O(n * max_deadline), as for each job, we may iterate over all possible slots up to its deadline.
#    - In the worst case, each job could be checked for up to max_deadline slots.

# 4. Collecting the scheduled jobs:
#    - Time complexity: O(max_deadline), as we iterate over the schedule array to collect the jobs.

# Overall time complexity:
# - Best-case time complexity: O(n log n) (if each job can be easily scheduled into its available slot).
# - Average-case time complexity: O(n log n + n * max_deadline).
# - Worst-case time complexity: O(n log n + n * max_deadline), where max_deadline is the largest deadline in the set of jobs.

# Space complexity:
# - Space complexity: O(n + max_deadline), as we need space for the schedule array (max_deadline) and to store the jobs (n).
