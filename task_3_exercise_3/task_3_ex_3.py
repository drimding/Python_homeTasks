"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import os
import fnmatch
import argparse


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """

    #
    def get_attr_file(path_file):
        # get int code of file access attributes
        file_attr = oct(os.stat(path_file).st_mode)[-3:]
        # convert int code to str access pattern
        file_str_attr = '-'
        attr_dict = {'0': '---',
                     '1': '--x',
                     '2': '-w-',
                     '3': '-wx',
                     '4': 'r--',
                     '5': 'r-x',
                     '6': 'rw-',
                     '7': 'rwx'}
        for i in file_attr:
            file_str_attr += attr_dict[i]
        return file_str_attr

    # Finding files by pattern and  return result dict {path + file name : file attribute}
    result = {}
    dir_entries = os.scandir(path)
    for entry in dir_entries:
        if fnmatch.fnmatch(entry.name, pattern):
            file_path_name = path + "/" + entry.name
            result[file_path_name] = get_attr_file(file_path_name)
    return result


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    # Your code
    for k in file_paths:
        print(k, file_paths.get(k))
    print(f'Found {len(file_paths)} file(s).')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('-p', type=str)
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()
