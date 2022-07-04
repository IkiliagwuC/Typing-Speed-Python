
from time import time

# to calculate the accuracy of the input prompt


def tperror(prompt):
    global inwords

    words = prompt.split()
    errors = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)):
            if inwords[i] == words[i]:
                continue
            else:
                errors = errors + 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) and (inwords[i - 1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
        return errors

# now to calculate the speed of words typed per minute


def speed(inprompt, stime, etime):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time

    return speed

# calculate the total elapsed time


def elapsedtime(stime, etime):
    time = etime - stime  # etime is the end time and stime is the start time
    return time


if __name__ == "__main__":
    prompt = "python is an interpreted high level general purpose programming languatge created by Guido van Rossum and first released in 1991, python is often described as 'batteries indluded' language due to its comprehensive standard library"
    # this is the paragraph you will type to check your speed
    print("Type this :- ", prompt)

    # checking to input Enter basically it will see
    print("###################################")
    input("Please press Enter when you are ready to check your speed ")
    print("###################################")

    # recording time for input
    stime = time()
    inprompt = input()
    etime = time()

    # collect all the information returned by the functions
    time = round(elapsedtime(stime, etime), 2)  # round of the time to 2dp
    speed = speed(inprompt, stime, etime)
    errors = tperror(prompt)

    # printing required data to see the result
    print("###################################")
    print("Total time elapsed:", time, "seconds")
    print("Your Average Typing speed was", speed, "words per minute (w/m)")
    print("with the total of ", errors, "errors")
    print("###################################")
