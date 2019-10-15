import os
import fibonacci

def get_files_in_folder(dirpath):
    result = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            result.append(filename)
    return result


def test_get_files_in_folder():
    print(get_files_in_folder("/home"))
    pass


def test_fibonacci():
    results = fibonacci.fib(100)
    print(results)
    
    fibonacci.fib2(100)
    
    print("fibonacci.FIB_MAX = {0}".format(fibonacci.FIB_MAX))
    
    print("fibonacci.__name__ = {0}".format(fibonacci.__name__))
    
    help(fibonacci)


def main():
    test_get_files_in_folder()

if __name__=="__main__":
    main()
