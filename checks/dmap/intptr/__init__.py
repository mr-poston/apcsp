import check50
import check50.c

@check50.check()
def compiles():
  """intptr.c compiles"""
  check50.run("make intptr").exit(0)

@check50.check()
def output():
  """Output is correct"""
  check50.run("./intptr").stdout("42 is at 0x.*", regex=True).exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./intptr").stdout("42 is at 0x.*", regex=True).exit(0)
