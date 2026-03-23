from ast import literal_eval

filename: str = "students.txt"

data: list = []


def loader() -> list:
    try:
        file = open(filename)
        raw_data: str = file.readlines()
        [data.append(literal_eval(temp_data)) for temp_data in raw_data]
    except Exception as e:
        print(f"Error: {e}")
    finally:
        file.close()
    return data

def updater(new_data: list) -> None:
    try:
        file = open(filename, "w")
        new_data_str: str = ""
        [new_data_str.join(item) + "\n" for item in new_data]
        print(new_data_str)
        #file.write(new_data_str)
        #[file.write(str(item) + "\n") for item in new_data]

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
