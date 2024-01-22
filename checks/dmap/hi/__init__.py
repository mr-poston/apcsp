import check50

@check50.check()
def compiles():
  check50.run("make hi").exit(0)
