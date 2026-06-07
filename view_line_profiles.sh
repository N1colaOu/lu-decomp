cd ./build/
echo "--------------------------------------------------------------------------------------------------"
echo "With Pivoting:"
scalene view true_pivot.json --cli
echo "--------------------------------------------------------------------------------------------------"
echo "Without Pivoting:"
scalene view false_pivot.json --cli
cd ..