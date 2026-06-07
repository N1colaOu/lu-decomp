echo "Visualizing Times for a 100x100 LU Decomp"
scalene run -o false_pivot.json profiler_false.py
scalene run -o true_pivot.json profiler_true.py

mv *json ./build/