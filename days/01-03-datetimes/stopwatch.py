from datetime import datetime


def stopwatch():
    start_stamp = datetime.now()
    input('Stopwatch started press "enter" to stop..')
    stop_stamp = datetime.now()
    timer = stop_stamp - start_stamp
    return timer


def main():
    while True:
        print("::Stopwatch App::\nCommands: Start - Quit")
        selection = input("Enter a command: \n").lower()

        if selection == "quit":
            break
        elif selection == "start":
            timer = stopwatch()
            print("Stopwatch stopped with a total time of {}\n".format(timer))
        else:
            print("Not a command\n")


if __name__ == "__main__":
    main()
