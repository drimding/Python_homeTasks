"""
Implement a function `sort_names(input_file_path: str, output_file_path: str) -> None`, which sorts names from
`file_path` and write them to a new file `output_file_path`. Each name should start with a new line as in the
following example:
Example:

Adele
Adrienne
...
Willodean
Xavier
"""


def sort_names(input_file_path: str, output_file_path: str) -> None:
    word_list = []
    with open(input_file_path, "r") as f:
        for line in f:
            word_list.append(line)
    with open(output_file_path, "w") as f:
        f.writelines(sorted(word_list))  # write sorted list

