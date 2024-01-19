import check50

@check50.check()
def memeory_leaks():
    check50.c.valgrind("./memory_practice").stdout()
