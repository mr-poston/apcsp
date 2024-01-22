import check50
import check50.c

@check50.check()
def compiles():
  """concatenate.c compiles"""
  check50.run("make concatenate").exit(0)

@check50.check()
def output1():
  """Output is correct"""
  check50.run("./concatenate").stdin("black cat").stdout("blackcat", regex=True).exit(0)

@check50.check()
def output2():
  """Output is correct"""
  check50.run("./concatenate").stdin("home run").stdout("homerun", regex=True).exit(0)

@check50.check()
def output3():
  """Output is correct"""
  check50.run("./concatenate").stdin("super charger").stdout("supercharger", regex=True).exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./concatenate").stdin("a b").stdout("ab", regex=True).exit(0)
