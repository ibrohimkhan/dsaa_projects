import os

def find_files(suffix, path):
    if os.path.isfile(path):
        if suffix is not None and len(suffix) > 0:
            if not path.endswith(f".{suffix}"):
                return None
            else:
                return os.path.basename(path)
        else:
            return os.path.basename(path)

    if not suffix:
        return None

    items = os.listdir(path)
    if not items:
        return None

    files = [file for file in items if os.path.isfile(path + '/' + file) and file.endswith(f".{suffix}")]
    folders = [folder for folder in items if os.path.isdir(path + '/' + folder)]

    for folder in folders:
        files.extend(find_files(suffix, path + '/' + folder))

    return files


def test_1():
    print("test 1: Normal case")
    base_dir = os.getcwd() + '/testdir'
    b = os.path.isdir(base_dir)
    print(find_files('c', base_dir))
    # returns ['t1.c', 'b.c', 'a.c', 'a.c']


def test_2():
    print("test 2: Edge case with no suffix")
    base_dir = os.getcwd() + '/testdir'
    b = os.path.isdir(base_dir)
    print(find_files('', base_dir))
    # returns None


def test_3():
    print("test 3: Edge case with no existing suffix")
    base_dir = os.getcwd() + '/testdir'
    b = os.path.isdir(base_dir)
    print(find_files('x', base_dir))
    # returns []


def test_4():
    print("test 4: Edge case where path of directory is path of a file")
    base_dir = os.getcwd() + '/testdir/t1.h'
    b = os.path.isdir(base_dir)

    print(find_files('h', base_dir))
    # returns t1.h

    print(find_files('', base_dir))
    # returns t1.h

    print(find_files('x', base_dir))
    # returns None


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()