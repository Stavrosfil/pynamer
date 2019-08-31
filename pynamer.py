import os
import re

basepath = 'testing/'
prefix = 'wall_'
extensions = '(jpg|png)'


def pl():
    print('----------------------------------')


# Detects int in string and returns is as int
def atoi(text):
    return int(text) if text.isdigit() else text


# Used for natural sorting of a string list.
# Splits any string in parts, and detects the ones containing numbers.
# Extracts the incremental name ID to do natural sorting.
def natural_keys(text):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    # Splits string whenever digits are found and returns the index found.
    # \d: Detect digit.
    # + : Matches one to unlimited times.
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def extract_id(text):
    return natural_keys(text)[1]


# Returns true if the string given matches our naming scheme.
def matches_name(name):
    return bool(re.match(prefix + r"[0-9]+\." + extensions, name))


def files_to_rename(prefix, extensions):
    _files_to_rename = []
    _maxNum = 0
    _filesIterator = os.scandir(basepath)

    print('\nFiles not matching :')
    pl()

    for f in _filesIterator:
        if f.is_file():
            # The files to rename must be image files or be already named correctly.
            if not matches_name(f.name):
                if bool(re.match(r".+\." + extensions, f.name)):
                    _files_to_rename.append(f.name)
            else:
                _maxNum = max(extract_id(f.name), _maxNum)

    # Natural sort.
    # Also see natsort package.
    _files_to_rename.sort(key=natural_keys)

    print(_files_to_rename)

    pl()

    return (_files_to_rename, _maxNum)


def rename_files(file_names_list, max_index):
    i, j = max_index + 1, 1
    _temp_files = []

    print('Preparing to rename image files :')
    pl()

    for file_name in file_names_list:
        suffix = os.path.splitext(file_name)[1]
        temp_name = str(j) + '_temp' + suffix
        os.rename(file_name, temp_name)
        _temp_files.append(temp_name)
        j += 1

    for file_name in _temp_files:
        suffix = os.path.splitext(file_name)[1]
        newName = prefix + str(i) + suffix
        print(file_name + '\t-->\t' + newName)
        os.rename(file_name, newName)
        i += 1

    pl()


def add_to_readme(wall):
    pass


def saveReadme():
    readme = ''
    file_names_list = os.listdir(basepath)
    file_names_list.sort(key=natural_keys)
    for f in file_names_list:
        if matches_name(f):
            readme += '* ### ' + f + '\n'
            readme += '![img](' + f + ')\n'

    print('Updating readme...')
    pl()

    f = open(basepath + 'README.md', 'w')
    f.write(readme)
    print(readme)
    f.close()

    pl()


def main():

    # Get the sorted files list to rename.
    files_to_rename_list, max_index = files_to_rename(prefix, extensions)

    # Rename the files using the sorted list
    rename_files(files_to_rename_list, max_index)

    saveReadme()


if __name__ == "__main__":
    main()
