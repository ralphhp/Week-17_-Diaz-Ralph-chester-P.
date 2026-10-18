def get_initial_readings():
    "Return the starting list of simulated device temperatures."
    return [28, 31, 35, 37, 29]

def is_whole_number(text):
    "Check whether the input contains digits, with an optional minus sign."
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] < "0" or text[index] > "9":
            return False
    return True

def classify_reading(reading, warning_limit, critical_limit):
    "Return NORMAL, WARNING, or CRITICAL for one reading."
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"

def display_readings(readings):
    "Display all readings in the list."
    print("\nCURRENT READINGS")
    print("----------------")

    for index in range(len(readings)):
        print("Reading", index + 1, ":", readings[index], "°C")

def add_reading(readings, lowest, highest):
    "Validate a new reading and add it only if it is valid."
    text = input("Enter new reading: ")

    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    else:
        reading = int(text)

        if reading < lowest or reading > highest:
            print("Invalid reading. Enter a value from", lowest, "to", highest, ".")
        else:
            readings.append(reading)
            print("Reading added successfully.")


def compute_total(readings):
    "Calculate the total by adding each reading in a loop."
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    "Calculate and return the average of the readings."
    total = compute_total(readings)
    return total / len(readings)


def find_minimum(readings):
    "Find the smallest reading by comparing values in a loop."
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    "Find the largest reading by comparing values in a loop."
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    "Count how many readings belong to one category."
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    "Return the overall status based on the category counts."
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_classifications(readings, warning_limit, critical_limit):
    "Display the category of each reading."
    print("\nREADING CLASSIFICATION")
    print("----------------------")

    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(reading, "°C ->", category)


def display_summary(readings, warning_limit, critical_limit):
    "Display numerical totals, category counts, percentages, and status."
    number = len(readings)
    total = compute_total(readings)
    average = compute_average(readings)
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print("\nMONITORING SUMMARY")
    print("------------------")
    print("Number of readings:", number)
    print("Total of readings:", total)
    print("Average temperature:", format(average, ".2f"), "°C")
    print("Minimum temperature:", minimum, "°C")
    print("Maximum temperature:", maximum, "°C")
    print()
    print("NORMAL:", normal_count, "(", format(normal_count / number * 100, ".2f"), "%)")
    print("WARNING:", warning_count, "(", format(warning_count / number * 100, ".2f"), "%)")
    print("CRITICAL:", critical_count, "(", format(critical_count / number * 100, ".2f"), "%)")
    print()
    print("Overall Status:", determine_overall_status(warning_count, critical_count))


def display_menu():
    "Display the five menu choices."
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    "Run the menu until the user chooses to exit."
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
