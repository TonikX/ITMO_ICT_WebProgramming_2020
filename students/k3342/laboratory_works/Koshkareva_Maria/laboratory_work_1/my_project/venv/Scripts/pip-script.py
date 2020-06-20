#!D:\hey_uni\3\Web\ITMO_ICT_WebProgramming_2020\students\k3342\laboratory_works\Koshkareva_Maria\laboratory_work_1\my_project\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==10.0.1','console_scripts','pip'
__requires__ = 'pip==10.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pip==10.0.1', 'console_scripts', 'pip')()
    )
