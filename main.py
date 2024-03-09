print("Enter the vertex of the top of the plateau ")
x, y = map(int, input().split())
while True:
    try:
        print("Enter the Co-ordinates of the ROVER")
        ix, iy = map(int, input().split())
        if ix < 0 or iy < 0 or ix > x or iy > y:
            raise Exception("Enter the Co-ordinates of the rover within the plateau")

        while True:
            setdir = input("Enter the direction of the rover ")[0]
            if setdir not in ["N", "S", "E", "W"]:
                print("Invalid direction. Please enter 'N', 'S', 'E', or 'W'.")
            else:
                break

        while True:
            cmd = input("Enter the movement of the rover")
            if cmd == "":
                print("Invalid command. Please enter a valid command.")
            elif any(c not in ["L", "M", "R"] for c in cmd):
                print("Invalid command. Please enter only 'L', 'M', or 'R' characters.")
            else:
                break

        
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
            raise Exception("Rover is out of the plateau")
        else:
            print("Final Co-ordinates of the rover", ix, iy, setdir)

    except Exception as e:
        print("Error occurred: ", str(e))
        continue
    except EOFError:
        break
