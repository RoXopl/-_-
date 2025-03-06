def func(code, setting):
    end = [""]

    n = 0
    x = True

    for i in code:

        if "y" in setting and i == setting["y"] and x:                    
            if "z" in setting:
                if setting["z"] == 0 or setting["z"] == 2:
                    end.append("")
                    n += 1

            end[n] += i
            x = False

        elif "y" in setting and i == setting["y"] and not x:
            end[n] += i
            x = True
            
            if "z" in setting:
                if setting["z"] == 0 or setting["z"] == 1:
                    end.append("")
                    n += 1

        elif "x" in setting and i == setting["x"] and x:
            end.append("")
            n += 1

        else:
            end[n] += i

    n = len(end) - 1

    while True:
        if end[n] == "":
            end.pop(n)
        if n == 0:
            break
        n -= 1

    return end