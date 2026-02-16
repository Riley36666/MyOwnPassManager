
filepath = "passwords/password.txt"


def deletePassFromFile(index, file_path=filepath):
    try:
        with open(file_path, "rb") as file:
            lines = file.readlines()

        if index < 1 or index > len(lines):
            raise IndexError("Invalid index")

        # Remove the selected line
        del lines[index - 1]

        with open(file_path, "wb") as file:
            file.writelines(lines)

        return True

    except (IndexError, FileNotFoundError) as e:
        print(f"Error deleting password: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error deleting password: {e}")
        return False

    
    except IndexError:
        print("Invalid index.")
    except FileNotFoundError:
        print("No passwords stored yet.")



def deleteAll():
    with open(filepath, "wb") as file:
        file.write(b"")