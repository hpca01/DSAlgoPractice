import os

def walk(extension, directory, output):
    if not os.path.exists(directory):
        print(f'Directory {directory} not found')
        return
    if os.path.exists(directory) and os.path.splitext(directory)[1] == extension:
        output.append(directory)
        return
    for each in os.listdir(directory):
        fpth = os.path.join(directory, each)
        _, file_ext = os.path.splitext(fpth)
        if os.path.isfile(fpth) and file_ext == extension:
            output.append(fpth)
        elif os.path.isdir(os.path.join(directory, each)):
            walk(extension, os.path.join(directory, each), output)

def find_files(suffix, path):
    filepaths = []
    walk(suffix, path, filepaths)
    return filepaths

def test1():
    print(find_files('.c', 'testdir'))

def test2():
    print(find_files(".h", "testdir"))

def test3():
    print(find_files(".c", "testdir/t1.c"))


if __name__ == "__main__":
    test1()
    test2()
    test3()