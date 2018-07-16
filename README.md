# Introduction

This program takes as input a text file containing data on which prescribers
have prescribed which drugs, and at what cost, from an online pharmacy. The
program outputs a text file with a list of the drugs that have been prescribed,
and for each drug, displays the number of unique individuals who prescribed it
and the total cost.

# Approach

The program starts by reading in the provided data and cleaning it. It creates
a dictionary in which the keys are the names of the drugs prescribed, and the
values are lists that contain as elements the total cost of the drug and the
set of prescribers of that drug. That dictionary is then converted to a list in
which each element is itself a list of the name of a drug, its total cost, and
the number of unique prescribers it has. That list is then sorted according to
the total cost of the drug in descending order, with ties broken by the name of
the drug. Finally, the information in the sorted list is written to a text file
with fields separated by commas.

# Run Instructions

The program takes as input a file called `itcont.txt` in the directory
`pharmacy_counting/input`. To run the program, navigate to the top-level
directory and call:

```
./run.sh
```

To run the test suite, navigate to `insight_testsuite` and call:

```
./run_tests.sh
```
