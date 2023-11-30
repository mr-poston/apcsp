import check50
import check50.c
import re

@check50.check()
def exists():
    """temps.c exists"""
    check50.exists("temps.c")

@check50.check(exists)
def compiles():
    """temps.c compiles"""
    check50.c.compile("temps.c")

@check50.check(compiles)
def output_check():
    """Output is correct"""
    desired = "\\nAverage July Temperatures by City\\n\\n"
    check50.run("./temps").stdout("Phoenix: 107\nLas Vegas: 105\n.*: 97\n.*: 97\nDenver: 90\n.*: 85\n.*: 85\n.*: 82\n.*: 82\nSan Francisco: 66", regex=True).exit(0)
