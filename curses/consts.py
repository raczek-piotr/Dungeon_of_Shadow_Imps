# disable traceback
import sys
sys.excepthook = lambda exc_type, exc_value, traceback: sys.exit(1)


version = "DoSI_1.1"
path = ""