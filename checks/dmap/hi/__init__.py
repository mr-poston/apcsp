import check50
import check50.c

@check50.check()
def compiles():
  """hi.c compiles"""
  check50.run("make hi").exit(0)

@check50.check()
def output():
  """Output is correct"""
  check50.run("./hi").stdout("HI!").exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./hi").stdout("HI!").exit(0)
