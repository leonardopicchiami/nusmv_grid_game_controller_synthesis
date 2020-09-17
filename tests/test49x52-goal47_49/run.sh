#!/bin/bash


echo "Start the tests execution..."
echo "Start of test 49x52 with optimized synthesis algorithm..."

python3 ../../src/python/main.py -conf config.ini -v 1 -o output_optimized input_file.input 1> test49x52_optimized.out


echo "Test 49x52 with optimized synthesis algorithm: done."
echo "Start of test 49x52 with standard synthesis algorithm..."

python3 ../../src/python/main.py -conf config.ini -mode 0 -v 1 -o output_standard input_file.input 1> test49x52_standard.out


echo "Test 49x52 with standard synthesis algorithm: done."
echo "End of tests execution."
