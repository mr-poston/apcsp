import check50
import check50.c

@check50.check()
def memeory_leaks():
    check50.c.valgrind("./memory_practice").stdout("HI!\n17").exit(0)
