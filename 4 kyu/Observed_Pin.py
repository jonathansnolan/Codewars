import itertools
def get_pins(observed):
    x = len(observed)
    i = []


    buttons = {"1":["1","2","4"],
               "2":["1","2","5","3"],
               "3":["3","2","6"],
               "4":["4","1","5","7"],
               "5":["4","2","6","5","8"],
               "6":["3","5","6","9"],
               "7":["7","4","8"],
               "8":["7","8","5","9","0"],
               "9":["8","9","6"],
               "0":["8","0"]}

    x = [buttons [n] for n in observed]
    xx = list(itertools.product(*x))
    xxx = ["".join(n) for n in xx]
    return xxx
