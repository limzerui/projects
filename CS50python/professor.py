import random
import sys

def main():
    level=get_level()

    score=0

    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        answer=int(input(f"{x} + {y} = "))
        correct_answer=int(x+y)
        if answer== correct_answer:
            score+=1
            continue
        else:
            print("EEE")
            answer_2=int(input(f"{x} + {y} = "))
            if answer_2==correct_answer:
                continue
            else:
                print("EEE")
                answer_3=int(input(f"{x} + {y} = "))
                if answer_3==correct_answer:
                    continue
                else:
                    print("EEE")
                    print(f"{x} + {y} = {correct_answer}")
                    continue
    total_score=int(score)
    print("Score: ", total_score)
    sys.exit()

def get_level():
    while True:
        try:
            lvl=int(input("Level:"))
            if lvl==1 or lvl==2 or lvl==3:
                return lvl
        except ValueError:
            pass

def generate_integer(n):
    if n==1:
        return random.randint(0, 9)
    elif n==2:

        return random.randint(10, 99)
    elif n==3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
