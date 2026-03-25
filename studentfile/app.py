filename = "students.txt"
data = []

def load() -> None:
    try:
        with open(filename, "r") as file:
            # strip() handles extra whitespace and newlines safely
            lines = [line.strip() for line in file if line.strip()]
        data.clear()
        data.extend(lines)
    except FileNotFoundError:
        with open(filename, "w") as f: pass # Create file if missing

def save_to_file() -> None:
    try:
        with open(filename, "w") as file:
            for item in data:
                file.write(item + "\n")
    except Exception as ex:
        print(f"Error saving: {ex}")

def update_student(*args) -> None:
    load()
    target_id = args[0]
    for i, item in enumerate(data):
        flds = item.split(",")
        if flds[0] == target_id:
            # Convert flds to list to modify, then join back
            flds_list = list(flds)
            # Update fields based on args provided (up to length of args)
            for index in range(1, len(args)):
                if index < len(flds_list):
                    flds_list[index] = args[index]
            
            data[i] = ",".join(flds_list)
            save_to_file()
            return
    print("Student not found.")

def getall() -> None:
    load()
    if not data:
        print("No records found.")
        return
    for item in data:
        flds = item.split(",")
        print("".join(f"{f.upper():<20}" for f in flds))

# Usage
getall()
update_student('1002', 'bonifacio', 'undress', 'bsit', '3')
print("\nAfter Update:")
getall()
