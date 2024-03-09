def roverpos(x: int, y: int, *test_cases):
    results = []
    for test_case in test_cases:
        try:
            ix, iy, setdir, cmd = test_case
            if ix < 0 or iy < 0 or ix > x or iy > y:
                results.append(None)
                continue
            
            setdir = setdir.upper()
            modx, mody = 0, 0

            if setdir == "N":
                mody = 1
            elif setdir == "S":
                mody = -1
            elif setdir == "E":
                modx = 1
            elif setdir == "W":
                modx = -1

            for c in cmd:
                if c == "R":
                    if setdir == "N":
                        setdir = "E"
                        modx, mody = 1, 0
                    elif setdir == "S":
                        setdir = "W"
                        modx, mody = -1, 0
                    elif setdir == "E":
                        setdir = "S"
                        modx, mody = 0, -1
                    elif setdir == "W":
                        setdir = "N"
                        modx, mody = 0, 1
                elif c == "L":
                    if setdir == "N":
                        setdir = "W"
                        modx, mody = -1, 0
                    elif setdir == "S":
                        setdir = "E"
                        modx, mody = 1, 0
                    elif setdir == "E":
                        setdir = "N"
                        modx, mody = 0, 1
                    elif setdir == "W":
                        setdir = "S"
                        modx, mody = 0, -1
                elif c == "M":
                    ix += modx
                    iy += mody

            if ix < 0 or iy < 0 or ix > x or iy > y:
                results.append(None)
            else:
                results.append((ix, iy, setdir))

        except Exception as e:
            results.append(None)
    return results
