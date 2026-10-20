# Question 1 - Logic Challenge
#
# Just a simulation of the BOX machine from the problem image.
# "DOUBLE - JUMP X" on LINE Y means: double BOX X, then jump to LINE (Y + X).
# Everything else is a straight read of the instructions into if/elif branches.

def run():
    box = {1: 860, 2: 15, 3: 1, 4: 1, 5: 3}
    answer = {"A": None, "B": None}

    line = 1
    while True:
        if line == 1:
            box[5] *= 2
            line = line + 5

        elif line == 2:
            box[3] *= 2
            line = line + 3

        elif line == 3:
            box[2] = box[2] + box[5]
            line = 7

        elif line == 4:
            answer["A"] = box[3]
            line = 1

        elif line == 5:
            box[4] = box[4] + box[3]
            line = 3

        elif line == 6:
            box[3] = box[3] + box[4]
            line = 2

        elif line == 7:
            line = 9 if box[2] > 100 else 8

        elif line == 8:
            line = 4 if box[2] > 50 else 1

        elif line == 9:
            answer["B"] = box[3]
            line = 10

        elif line == 10:  # STOP
            break

        else:
            raise RuntimeError(f"Unknown line number: {line}")

    return answer, box


if __name__ == "__main__":
    answer, final_boxes = run()
    print("Final BOX values:")
    for i in range(1, 6):
        print(f"  BOX {i} : {final_boxes[i]}")
    print()
    print(f"ANSWER - BOX A : {answer['A']}")
    print(f"ANSWER - BOX B : {answer['B']}")
