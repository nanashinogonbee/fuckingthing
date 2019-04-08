import random
import sys
import os
import traceback

if __name__ == '__main__':
    print(f'Import this module via "import {sys.argv[0].split(".")[0]}".')
else:
    try:
        path = os.path.dirname(sys.argv[0])
        full_path = f'{os.path.abspath(path)}/{sys.argv[0]}'
        script = open(full_path).readlines()
        imports = [i for i in script if i.startswith('import ')]
        raise ModuleNotFoundError(random.choice(imports))
    except ModuleNotFoundError as e:
        tb = traceback.format_exc().strip().splitlines()
        module = tb[-1].split()[-1]
        path = os.path.dirname(sys.argv[0])
        full_path = f'{os.path.abspath(path)}/{sys.argv[0]}'
        script = open(full_path).readlines()
        imports = [i for i in script if i.startswith('import ')]
        imports = [' '.join(i.split()[1:]) for i in imports]
        import_lines = [i + 1 for i in range(len(script)) if script[i].startswith('import ')]
        err_line = import_lines[imports.index(module)]
        tb[1] = f'  File "{full_path}", line {err_line}, in <module>'
        tb[2] = f'  import {module}'
        tb[3] = f'ModuleNotFoundError: No module named \'{module}\''
        for line in tb:
            print(line, file=sys.stderr)
        sys.exit()
