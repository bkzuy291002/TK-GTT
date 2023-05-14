def max_value_job_assignment(jobs): #trả về giá trị lớn nhất có thể đạt được khi phân công các công việc
    n = len(jobs)
    # Sort jobs by their finish time
    jobs.sort(key=lambda x: x[1])
    # Initialize dynamic programming table
    dp = [0] * n
    # Set base case
    dp[0] = jobs[0][2]
    # Compute maximum value for each job assignment
    for i in range(1, n):
        value = jobs[i][2]
        # Find the latest job that finishes before the start of the current job
        j = i - 1
        while j >= 0 and jobs[j][1] > jobs[i][0]:
            j -= 1
        if j >= 0:
            value += dp[j]
        # Take the maximum value between taking the current job and not taking it
        dp[i] = max(dp[i-1], value)
    return dp[-1]
jobs = [(0, 4, 3), (2, 6, 4), (4, 7, 2), (5, 9, 6)]
# công việc thứ nhất bắt đầu vào thời điểm 0, kết thúc vào thời điểm 4 và có giá trị là 3. 
# Công việc thứ hai bắt đầu vào thời điểm 2, kết thúc vào thời điểm 6 và có giá trị là 4, 
# và cứ tiếp tục như vậy cho các công việc còn lại.
print(max_value_job_assignment(jobs))
