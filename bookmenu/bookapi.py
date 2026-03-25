filename: str = "books.txt"
data: list = []


def load() -> None:
    try:
        with open(filename, "r") as file:
            # strip() handles extra whitespace and newlines safely
            lines = [line.strip() for line in file if line.strip()]
        data.clear()
        data.extend(lines)
    except FileNotFoundError:
        with open(filename, "w+") as f:
            pass


def save_to_file() -> None:
    try:
        with open(filename, "w") as file:
            for item in data:
                file.write(item + "\n")
    except Exception as ex:
        print(f"Error saving: {ex}")


def update_book(*args) -> None:
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
    print("Book not found.")


def add_book(*args) -> None:
    load()
    if not args:
        print("No book data provided.")
        return

    # Store records in the same CSV format that `update_book()` / `getall()` expect.
    bookdata = ",".join(str(i).strip() for i in args)
    data.append(bookdata)
    save_to_file()
    print(data)

def find_book(isbn: str) -> list:
    load()
    for item in data:
        fields: list = item.split(",")
        if fields[0] == isbn:
            return fields
        
    return []


def getall() -> None:
    load()
    if not data:
        print("No records found.")
        return
    for item in data:
        flds = item.split(",")
        print("".join(f"{f.upper():<20}" for f in flds))
