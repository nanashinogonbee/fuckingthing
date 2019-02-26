import random
import sys
import os
import traceback

if __name__ == '__main__':
    print(f'Import this module via "import {sys.argv[0].split(".")[0]}".')
else:
    try:
        raise ModuleNotFoundError(random.choice(dir()))
    except Exception as e:
        tb = traceback.format_exc().splitlines()
        module = tb[-1].split()[-1]
        path = os.path.dirname(sys.argv[0])
        full_path = f'{os.path.abspath(path)}/{sys.argv[0]}'
        tb[1] = f'  File "{full_path}", line 9, in <module>'
        tb[2] = f'  import {module}'
        for line in tb:
            print(line)
        sys.exit()
