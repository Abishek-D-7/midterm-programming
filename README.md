# CMPSC 202 - Midterm Programming Assignment

Name: Abishek Dhakal

**Instructions**: Complete the exercise below. Open book, open notes, any tools allowed (except submitting another student's work). Due tonight (10/6) at 11:59pm.

**Submission**: Fork this repository and invite your professor (username: bcmullins) to the repository. To submit, push your code to your forked repository. Make sure to include your name in the README file.

You have been provided with a starter Python file (`midterm_starter.py`). This file contains two fully implemented algorithms that solve the exact same problem: finding if an array contains duplicate values.

The file also contains a `flawed_benchmark()` function. The developer who wrote this benchmark made several severe methodological errors, making the printed timing results completely unreliable for comparing the asymptotic growth of these two algorithms.

**Your tasks**: 

1. Rewrite the `flawed_benchmark()` function to provide a robust empirical comparison of the two algorithms. List the methodological errors in the original benchmark and explain how you fixed them. Your benchmark should demonstrate the scaling behavior of the two algorithms across multiple input sizes.

Methodological errors and fixes:

- **The original benchmark included data generation in the timing.** I moved the list creation and shuffling before the timer starts so I could measure the algorithms themselves, with only a small amount of loop overhead.
- **The algorithms used different random lists.** I gave both algorithms the same list at each input size to make the comparison fair. I also used a fixed random seed so I could reproduce the input order.
- **Random duplicates could make the algorithms stop early.** I used unique integers so both algorithms have to check the whole list. This helps show the slow algorithm's quadratic growth and the fast algorithm's expected linear growth. My results describe inputs with no duplicates; inputs with duplicates may finish sooner.
- **The benchmark tested only one input size.** I tested lists with 250, 500, 1,000, 2,000, and 4,000 elements so I could see how the running times change as the input size doubles.
- **Each algorithm was timed only once.** I warmed up both algorithms and measured each one over seven trials. I also timed batches of calls that took at least about 20 milliseconds, then divided by the number of calls to get the time per call. I reported the median to reduce the effect of unusually slow trials.
- **The timer and execution order could affect the comparison.** I replaced `time.time()` with `time.perf_counter()`, which is better suited for measuring short durations. I also alternated which algorithm ran first between trials to reduce any advantage from always running in the same order. The timings can still vary depending on the computer and other programs running.

2. Run the empirical comparion and plot the results using a plotting library of your choice (e.g., `matplotlib`, `seaborn`, etc.). Include the plot in your submission called `results.png`. Be sure to label your axes and include a legend.
