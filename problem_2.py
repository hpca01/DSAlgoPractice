import os

def walk(directory):
    if not os.path.exists(directory):
        print(f'Directory {directory} not found')
        return
    print(directory)
    for each in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, each)):
            print(f'{os.path.join(directory, each)}')
        elif os.path.isdir(os.path.join(directory, each)):
            walk(os.path.join(directory, each))

def test1():
    walk('testdir')
        # ./testdir
        # ./testdir/subdir1
        # ./testdir/subdir1/a.c
        # ./testdir/subdir1/a.h
        # ./testdir/subdir2
        # ./testdir/subdir2/.gitkeep
        # ./testdir/subdir3
        # ./testdir/subdir3/subsubdir1
        # ./testdir/subdir3/subsubdir1/b.c
        # ./testdir/subdir3/subsubdir1/b.h
        # ./testdir/subdir4
        # ./testdir/subdir4/.gitkeep
        # ./testdir/subdir5
        # ./testdir/subdir5/a.c
        # ./testdir/subdir5/a.h
        # ./testdir/t1.c
        # ./testdir/t1.h

def test2():
    walk('.')
    # lists everything in current directory + the output from test 1

def test3():
    walk('not_exists')
    # should print that directory doesn't exist

if __name__ == "__main__":
    test1()
    test2()
    test3()