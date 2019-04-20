def bracket_check(tst: str):
    while "()" in tst:
        tst = tst.replace("()", '')

    print("YES") if not tst else print("NO")
