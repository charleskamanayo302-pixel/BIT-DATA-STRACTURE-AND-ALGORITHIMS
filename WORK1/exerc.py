# -------------------------------
# Library Fine Calculator Project
# -------------------------------

import array

# 1. INTEGERS
fines = [100, 200, 50, 150, 300]   # fine amounts in RWF
total = sum(fines)
average = total / len(fines)
minimum = min(fines)
maximum = max(fines)

print("---- Integer Calculations ----")
print(f"Fines: {fines}")
print(f"Total: {total}, Average: {average}, Min: {minimum}, Max: {maximum}\n")

# 2. STRINGS (report with f-strings)
print("---- String Report ----")
report = f"The total library fines collected: {total} RWF.\n"
report += f"The average fine per student: {average:.2f} RWF."
print(report + "\n")

# 3. BOOLEANS (threshold condition + compound condition)
threshold = 180
if average > threshold and maximum > 250:  # compound condition
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# 4. LISTS (records of student fines)
print("---- List Operations ----")
student_fines = [120, 200, 300, 150, 50]
print("Original fines list:", student_fines)

# Add new fine
student_fines.append(180)

# Remove a fine if less than 100
student_fines = [fine for fine in student_fines if fine >= 100]

# Sort list
student_fines.sort()
print("Modified and sorted fines list:", student_fines, "\n")

# 5. ARRAYS (fixed-size subset)
print("---- Array Operations ----")
fines_array = array.array('i', [100, 200, 150, 50, 300])
array_sum = sum(fines_array)
list_sum = sum(student_fines)

print("Array fines:", fines_array.tolist())
print("Sum of array:", array_sum)
print("Sum of list:", list_sum)
print("Comparison: ", "Equal" if array_sum == list_sum else "Not Equal", "\n")

# 6. DICTIONARIES (records with id, name, value)
print("---- Dictionary Operations ----")
records = [
    {"id": 1, "name": "Alice", "value": 120},
    {"id": 2, "name": "Bob", "value": 200},
    {"id": 3, "name": "Charlie", "value": 150}
]

# Update Bob's fine
for rec in records:
    if rec["id"] == 2:
        rec["value"] = 250

# Delete Charlie's record
records = [rec for rec in records if rec["id"] != 3]

# Compute total fines
total_value = sum(rec["value"] for rec in records)

print("Final records:", records)
print("Total fines from records:", total_value)
