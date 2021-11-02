
def file_opener(filename: str):
    """opening a given file. reads it and give it back by splitlines.

    Returns: list of list
    """

    with open(filename, "r") as file:
        return file.read().splitlines()


def save_csv_file(filename: str, file: list):
    """creates a .csv file"""

    with open(filename, "w") as csv_file:
        for line in file:
            csv_file.write(",".join(line))
            csv_file.write("\n")

