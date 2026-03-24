from ast import literal_eval

filename: str = "students.txt"

data: list = []


def loader() -> list:
    global data
    data.clear()  
    try:
        file = open(filename, "r")
        raw_data = file.readlines()
        for temp_data in raw_data:
            if temp_data.strip():
                data.append(literal_eval(temp_data))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        file.close()
    return data


def updater(new_data: list) -> None:
    try:
        file = open(filename, "w")
        for item in new_data:
            file.write(str(item) + "\n")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        file.close()


def appender() -> None:
    try:
        file = open(filename, "a")
        [file.write(str(item) + "\n") for item in data]

    except Exception as e:
        print(f"Error: {e}")
    finally:
        file.close()
