import random
import sys
import traceback

if __name__ == '__main__':
    print(f'Import this module via "import {sys.argv[0].split(".")[0]}".')
else:
    try:
        raise ModuleNotFoundError(random.choice(dir()))
    except Exception as e:
        tb = traceback.format_exc().splitlines()
        module = tb[-1].split()[-1]
        tb[2] = f'  import {module}'
        for line in tb:
            print(line)
