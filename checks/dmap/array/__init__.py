import check50
import check50.c

@check50.check()
def compiles():
  """array.c compiles"""
  check50.run("make array").exit(0)

@check50.check()
def output1():
  """Output is correct"""
  check50.run("./array").stdin("3", prompt=False).stdin("42", prompt=False).stdin("13", prompt=False).stdin("3", prompt=False).stdout("The sum is 58", regex=True).exit(0)

@check50.check()
def output2():
  """Output is correct"""
  check50.run("./array").stdin("2", prompt=False).stdin("11", prompt=False).stdin("9", prompt=False).stdout("The sum is 20", regex=True).exit(0)

@check50.check()
def output3():
  """Output is correct"""
  check50.run("./array").stdin("3", prompt=False).stdin("1", prompt=False).stdin("2", prompt=False).stdin("-3", prompt=False).stdout("The sum is 0", regex=True).exit(0)

@check50.check()
def memeory_leaks():
  """No memory leaks detected"""
  check50.c.valgrind("./array").stdin("1", prompt=False).stdout("The sum is 42", regex=True).exit(0)
