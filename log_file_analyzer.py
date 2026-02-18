
# Step 1: Read Log File
with open("server.log", "r") as file:
    lines = file.readlines()
    # print(lines)

    # Step 2: Initialize counters
    total = 0
    info_count = 0
    error_count = 0
    warning_count = 0
    errors = []

    # Step 3: Analyze logs
    for line in lines:
        total += 1
        if "INFO" in line:
            info_count += 1
        elif "ERROR" in line:
            error_count += 1
            errors.append(line.strip())
        elif "WARNING" in line:
            warning_count += 1

    # Step 4: Print Report
    print(f"Total logs: {total}")
    print(f"INFO: {info_count}")
    print(f"WARNING: {warning_count}")
    print("\nError Messages:")
    for err in errors:
        print(err)

    # Step 5: Save Summary to File
    with open("log_summary.txt", "w") as file:
        file.write(f"Total logs: {total}\n")
        file.write(f"INFO: {info_count}\n")
        file.write(f"ERROR: {error_count}\n")
        file.write(f"WARNING: {warning_count}\n")

