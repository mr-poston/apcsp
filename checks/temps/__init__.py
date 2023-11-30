import check50
import check50.c

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
    desired = "\nAverage July Temperatures by City\n\n"
    desired += "Phoenix: 107\n"
    desired += "Las Vegas: 105\n"
    desired += "Austin: 97\n"
    desired += "Miami: 97\n"
    desired += "Denver: 90\n"
    desired += "Chicago: 85\n"
    desired += "New York: 85\n"
    desired += "Boston: 82\n"
    desired += "Los Angeles: 82\n"
    desired += "San Francisco: 66"
    check50.run("./temps").stdout(desired).exit(0)