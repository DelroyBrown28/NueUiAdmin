#!"c:\Users\Delroy Brown\Desktop\NewCodeProjects\NueUiAdmin\virtual\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'docformatter==1.4','console_scripts','docformatter'
__requires__ = 'docformatter==1.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('docformatter==1.4', 'console_scripts', 'docformatter')()
    )
