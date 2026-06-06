echo "Visualizing Times for a 100x100 LU Decomp"
echo "Without pivoting:"
kernprof -lv profiler_false.py
echo "With pivoting:"
kernprof -lv profiler_true.py

mv *.lprof ./build/
