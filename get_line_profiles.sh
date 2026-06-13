echo "Generating Times for LU Decomp"
scalene run -o false_pivot.json profiler_false.py
scalene run -o true_pivot.json profiler_true.py

mkdir -p build
mv *json ./build/