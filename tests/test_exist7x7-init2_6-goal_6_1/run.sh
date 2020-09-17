#!/bin/bash


#python3 ../../src/python/main.py -path -conf config.ini -v 1 input_file.input


echo "Start the tests execution..."
echo "Start of the test to check if at least one path from (2, 6) to (6, 1) in a 7x7 grid..."

python3 ../../src/python/main.py -path -conf config.ini -v 1 input_file.input 1> test_exist7x7-init2_6-goal_6_1.out


echo "Test to check if at least one path from (2, 6) to (6, 1) in a 7x7 grid: done."
echo "End of test execution."