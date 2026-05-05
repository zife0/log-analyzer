import re

def analyze_log(file_path):
    errors = []
    warnings = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if re.search(r"error", line, re.IGNORECASE):
                    errors.append(line.strip())
                elif re.search(r"warning", line, re.IGNORECASE):
                    warnings.append(line.strip())

        print("=== Log Analysis ===")
        print(f"Errors found: {len(errors)}")
        print(f"Warnings found: {len(warnings)}")

        if errors:
            print("\nSample Errors:")
            for e in errors[:5]:
                print("-", e)

        if warnings:
            print("\nSample Warnings:")
            for w in warnings[:5]:
                print("-", w)

    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    log_file = input("Enter log file path: ")
    analyze_log(log_file)
