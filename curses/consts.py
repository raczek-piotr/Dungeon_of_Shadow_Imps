version = "DoSI_1.a"
path = ""

# disable traceback
from sys import excepthook, exit
excepthook = lambda exc_type, exc_value, traceback: exit(1)
