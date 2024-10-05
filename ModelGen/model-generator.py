import csv
import random
import sys

def build_data(data_size=1, small=-2**64, big=2**64):

    with open('math_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ['input', 'output']

        writer.writerow(field)

        #If need to can add more stuff to the list at op[0]
        ops = {
            "addition": ([" + "], lambda a,b : a + b), 
            "subtraction": ([" - "], lambda a,b : a - b), 
            "multiplication": ([" * "], lambda a,b : a * b), 
            "division": ([" / "], lambda a,b : round(a/b, 2) if a % b else int(a/b))
            }

        #Random Loop
        for i in range(data_size):
            try:
                op = ops[random.choice(list(ops.keys()))]
                a = random.randint(small, big)
                b = random.randint(small, big)
                if b == 0 and op == "division":
                    b = 1
                row = ["what is " + str(a) + random.choice(op[0]) + str(b), str(op[1](a,b))]
                writer.writerow(row)
            except KeyboardInterrupt:
                print("terminated with "+str(i)+" data points")
                break

def main():
    x = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    small = -2**64 if len(sys.argv) < 3 else int(sys.argv[2])
    big = 2**64-1 if len(sys.argv) < 4 else int(sys.argv[3])
    build_data(x, small, big)


if __name__ == "__main__":
    main()