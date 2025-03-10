

# SRC_DIR=$(pwd)/../common
# echo "SRC_DIR*******: $SRC_DIR"
# ls -l $SRC_DIR


# echo "Running test cases for NewsReader"
# echo "Source directory: $SRC_DIR"

# TEST_DIR=$(dirname $0)/testcases

# cd $TEST_DIR
# export PYTHONPATH=$PYTHONPATH:$SRC_DIR
# echo ${PYTHONPATH}
# # Run Pytest and generate report and coverage report
# pytest --cov=./reports --cov-report html --cov-report term


#!/usr/bin/env bash
# check if reports directory exists, if is there delete it
if [ -d "reports" ]; then
  rm -rf reports
fi

export PYTHONPATH=../common
cd testcases
pytest -s --cov=../common \
      --cov-report=html:reports/coverage_report \
      --junitxml=reports/test_report.xml \
      --html=reports/test_report.html