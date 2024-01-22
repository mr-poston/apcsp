import check50
import check50.c

@check50.check()
def compiles():
  """array.c compiles"""
  check50.run("make array").exit(0)

@check50.check()
def output1():
  """Output is correct"""
  check50.run("./array").stdin("3").stdin("42").stdin("13").stdin("3").stdout("The sum is 58", regex=True).exit(0)

@check50.check()
def output2():
  """Output is correct"""
  check50.run("./array").stdout("The sum is 20", regex=True).exit(0)

@check50.check()
def output3():
  """Output is correct"""
  check50.run("./array").stdin("3").stdin("1").stdin("2").stdin("-3").stdout("The sum is 0", regex=True).exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./array").stdin("1").stdout("The sum is 42", regex=True).exit(0)
