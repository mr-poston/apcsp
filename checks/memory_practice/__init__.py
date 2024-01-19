import check50

@check50.check()
def memeory_leaks():
    output = check50.run("valgrind ./memory_practice").stdout()
    fail = False
    message = ""
    if "LEAK SUMMARY:" in output:
        message += "Memory leak detected. "
        fail = True
    if "Invalid write of" in output:
        message += "Invalid write detected."
        fail = True
    if fail:
        raise check50.Failure(message) 