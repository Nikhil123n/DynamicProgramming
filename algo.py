import time, numpy
import matplotlib.pyplot as plt

def max_revenue(n, lengths, prices):
    # Initialize dp array where dp[i] is the maximum revenue achievable with i minutes
    dp = [0] * (n + 1)
    
    # Iterate over each time from 1 to n
    for i in range(1, n + 1):
        # Check all slot lengths to determine the maximum revenue for dp[i]
        for j in range(len(lengths)):
            if lengths[j] <= i:
                dp[i] = max(dp[i], dp[i - lengths[j]] + prices[j])

    # The maximum revenue achievable for `n` minutes is in dp[n]
    return dp[n]

def theoretical_time(n): 
    return (n * len(lengths))


# _____________________________________________________________________________________________________
lengths = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
prices = [5, 9, 13, 17, 20, 24, 27, 30, 35, 40]
theor_time = []
expt_time = []
n_Range = [10, 50, 100, 200, 500, 1000]
# n_Range = [100, 500, 1000, 5000, 10000, 20000]
m = len(lengths)

for n in n_Range:
    # Execute the Huffman coding algorithm
    startTime = time.perf_counter_ns()
    max_revenue(n, lengths, prices)
    endTime = time.perf_counter_ns()

    theor_time.append(theoretical_time(n))
    expt_time.append(endTime - startTime)

print(theor_time, expt_time)

# Scaling the theoretical values
theoretical_avg, experimental_avg = numpy.average(theor_time), numpy.average(expt_time)
scale_factor = experimental_avg / theoretical_avg  # Scale theoretical to match experimental times
for i in range(len(theor_time)):
    theor_time[i] *= scale_factor

print("Scaled Theoretical Time", theor_time)
print("Experimental Time", expt_time)

# _____________________________________________________________________________________________________________________
# Plotting
plt.figure(figsize=(12, 6))

# Plotting theoretical times
plt.plot(n_Range, theor_time, label="Theoretical Time (O(n * m))", marker='o')

# Plotting experimental times
plt.plot(n_Range, expt_time, label="Experimental Time", marker='x')

plt.ticklabel_format(style='plain')

plt.xlabel("Advertising Time (n)")
plt.ylabel("Time Complexity (in ns)")
plt.legend()

# Show the plot
plt.show()
