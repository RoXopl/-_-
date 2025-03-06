def func():
    from src.el._py import dax
    dat = ""

    setting = {
        "x":" ", #это то что будет разделять
        "y":'"', #это то что не разделяется пока не встретит вторую пару
        "z":0
    }

    while True:
        print(dat)
        cmd = input(">>> ")
        if cmd == "quit": quit()
        dat = dax.func(cmd, setting)