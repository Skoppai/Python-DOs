print("#################################P-DOS#################################")
drive = "C"
notepadInt = 0
import time
for i in range(1232):
    bSlash = str("\ ")
    dosCMD = input("{}:{}".format(drive, bSlash))
    if dosCMD == "dos":
        print("#################################MS-DOS#################################")
        print("\n\n\nP-DOS Python dock v1.0a ID: 14.07.20\n\n\nPython Shell")
    if dosCMD == "dir a":
        drive = "A"
    if dosCMD == "dir A":
        drive = "A"
    if dosCMD == "dir b":
        drive = "B"
    if dosCMD == "dir B":
        drive = "B"
    if dosCMD == "dir c":
        drive = "C"
    if dosCMD == "dir C":
        drive = "C"
    if dosCMD == "format":
        emergency = input("WARNING! EVERYTHING ON {} DRIVE WILL BE WIPED!".format(drive))
        if emergency == "y":
            print("▓░░░░░░░░░ 10%")
            time.sleep(2)
            for i in range(20):
                print(" ")
            print("▓▓▓░░░░░░░ 30%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓░░░░░░ 40%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓░░░░░ 50%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓░░░░ 60%")
            time.sleep(4)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓░░░░ 70%")
            time.sleep(0.09)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓░░ 80%")
            time.sleep(2)
            print("▓▓▓▓▓▓▓▓▓▓ 99%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓▓▓ 100%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓▓▓\nFormat Complete!")
            notepadNotes = ["EMPTY", "EMPTY", "EMPTY", "EMPTY",  "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", " ", " ", " ", " ", " "]
    if dosCMD == "reboot":
        emergency = input("There may be unsaved work. are you sure? (y/n) ")
        if emergency == "y":
            print("▓░░░░░░░░░ 10%")
            time.sleep(2)
            for i in range(20):
                print(" ")
            print("▓▓▓░░░░░░░ 30%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓░░░░░░ 40%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓░░░░░ 50%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓░░░░ 60%")
            time.sleep(4)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓░░░░ 70%")
            time.sleep(0.09)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓░░ 80%")
            time.sleep(2)
            print("▓▓▓▓▓▓▓▓▓▓ 99%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓▓▓ 100%")
            time.sleep(1)
            for i in range(20):
                print(" ")
            print("▓▓▓▓▓▓▓▓▓▓\nReboot Complete!")
    elif dosCMD == "write":
        notepadNotes = ["EMPTY", "EMPTY", "EMPTY", "EMPTY",  "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", "EMPTY", " ", " ", " ", " ", " "]
        notepadInput = input("Time to write! View Typing.txt before writing.\n")
        notepadNotes[notepadInt] = notepadInput
        print("This note has an ID of {}.".format(notepadInt))
        notepadInt = notepadInt+1
    elif dosCMD == "read":
        notepadInput = input("Enter your id: ")
        print(notepadNotes[int(notepadInput)])
    else:
        print("Invalid command.")
        