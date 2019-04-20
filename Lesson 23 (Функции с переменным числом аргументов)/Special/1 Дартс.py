def score(*args):
    if len(args) == 1:
        args = args[0]
        if args == "Яблочко":
            return 50
        if "зеленое" in args.lower():
            return 25

    return scoring[args[0]][args[1]]
