import os


def isBinod(fileName):
    with open(fileName, "r") as f:
        fileContent = f.read()
        if "binod" in fileContent.lower():
            return True
        else:
            return False


if __name__ == '__main__':
    dir_contents = os.listdir()
    print(dir_contents)
    for items in dir_contents:
        if items.endswith('txt'):
            print(f"detecting Binod in{items}")
            flag = isBinod(items)
            if (flag):
                print(f"Binod found in {items}")
            else:
                print("not found")
