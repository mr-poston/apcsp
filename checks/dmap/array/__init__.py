import check50
import check50.c

@check50.check()
def compiles():
  """array.c compiles"""
  check50.run("make array").exit(0)

@check50.check()
def output1():
  """Output is correct for [42, 13, 3]"""
  check50.run("./array").stdin("3 42 13 3").stdout("The sum is 58", regex=True).exit(0)

@check50.check()
def output2():
  """Output is correct for [11, 9]"""
  check50.run("./array").stdin("2 11 9").stdout("The sum is 20", regex=True).exit(0)

@check50.check()
def output3():
  """Output is correct for [1, 2, -3]"""
  check50.run("./array").stdin("3 1 2 -3").stdout("The sum is 0", regex=True).exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./array").stdin("1 42").stdout("The sum is 42", regex=True).exit(0)
