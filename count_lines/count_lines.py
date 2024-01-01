from pathlib import Path
import sys

# checking if argument passed is meeting the criteria line 5-9
if len(sys.argv) < 2:
    sys.exit ("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit ("Too many arguments")

#using pathlib library to distinguish between .py and .other (doctypes) line 12-14
path = Path(sys.argv[1])

#checks if the file is a .py file at the first place line 15-30
if path.suffix == ".py":
    #using try - except to check the file name if correct or incorrect line 17-27
    try:
        with open(sys.argv[1]) as file:
            count = 0
            for line in file:
                line = line.strip()
                if not (line.startswith("#")) and line:
                    count += 1
            print (count)

    except FileNotFoundError:
        sys.exit("File doesn't exist")
else:
    sys.exit ("Not a python file")