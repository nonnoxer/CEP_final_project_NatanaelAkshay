# Learning Journey Allocation

This learning journey (LJ) allocation program is designed to allocate students to certain LJ. This program takes in 2 separate files which contain all the necessary data and outputs 3 sets of files for convenience.
The program will first sort the applications by time submitted, before allocating students to various LJs according to time submitted, choice, and available slots. Invalid submissions will be allocated to the first LJ with available slots.

## Getting Started
### Prerequisites

In order to run this program, you will need to have [Python 3](https://www.python.org/downloads/) installed as this program runs using Python 3.

### Input

You will need a set of input files with the format of the following files (all in .csv format):

```
venuesExample.csv
choicesExample.csv
```

Ensure that all input files are in the same folder as the program.

### Usage

Upon starting this program, it will automatically request your 2 desired input files. After processing, it will output 3 sets of files. In case the program is stopped or is needed to be run again, you can type start() into the console.

### Output

The program will output 3 sets of files (all in .csv format):

1. The master output file containing the allocations of all the students
2. An output file for each class of students
3. An output file for each learning journey

## Built With

[Python 3](https://www.python.org/downloads/) - The programming language used

## Authors

* **Natanael Tan Tiong Oon**
* **Baskaran Akshay Kumar**

## Acknowledgments

Our teacher, Mrs Lorraine Neo, for helping and guiding us for our project
