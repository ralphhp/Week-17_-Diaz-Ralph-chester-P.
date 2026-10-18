# Simulated Device Monitoring and Alert System

**Student Name:** Ralph Chester P. Diaz 
**Student Number:** 2601287 
**Section:** 1CpE-B

## Project Description
This Python program simulates monitoring device-temperature readings. It stores readings in a list, classifies each temperature as NORMAL, WARNING, or CRITICAL, and produces a numerical summary. It is a classroom simulation and does not connect to a real device or sensor.

## Features
- View all stored temperature readings and their positions
- Add a whole-number reading from 0 to 100
- Reject empty, non-numeric, negative, and above-range readings
- Classify readings using the required temperature limits
- Calculate total, average, minimum, maximum, category counts, and percentages
- Determine the overall monitoring status
- Repeat the menu until the user chooses Exit

## Requirements
- Python 3

## How to Run
1. Open a terminal in the `Week17` folder.
2. Run `python device_monitor.py`.
3. If your computer uses the `python3` command, run `python3 device_monitor.py`.

## Sample Output
The initial readings are `28, 31, 35, 37, 29`. Choosing **Generate Summary** displays:

```text
MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL : 2 (40.00%)
WARNING : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## Test Cases
Ten planned test cases are listed in [test_cases.md](test_cases.md). Run them on your own computer and update the Actual Result and Pass/Fail columns to match what you observe.

## Known Limitations
- Readings are stored only while the program is running; they are not saved after the program closes.
- Temperatures are simulated and are not collected from real hardware.
- Only whole-number readings from 0 to 100 are accepted.

## Reflection
This project helped me combine lists, loops, selection statements, and functions in one program. One important part was validating input before converting it into an integer so invalid data would not enter the list. I also had to make sure the boundary values 30 °C and 35 °C are both classified as WARNING. In the future, I would improve the program by allowing readings to be saved between sessions and by connecting it to an actual sensor.
