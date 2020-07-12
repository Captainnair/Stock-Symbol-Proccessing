import os
import datetime


common = []


def time_stamp(name, fmt='{name}_%m-%d-%y.txt'):  # creates the time stamp for the program.
    return datetime.datetime.now().strftime(fmt).format(name=name)


def first_file(directory):
    """
    This piece of code is the code to append the list of stocks
    in the first file to a list that can be used later on to be
    compared to other lists
    """
    stepper = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            stepper += 1
            if stepper < 2:
                f = open('%s\\%s' % (directory, filename), 'rt')
                for line in f:
                    line = line.strip()
                    common.append(line)
            else:
                break
    return common


def common_stock(directory):
    time = datetime.datetime.now()  # creating the time from the time_stamp program.
    time = time.strftime("%m-%d-%y")
    starting = []
    first = first_file(directory)
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            starting.clear()
            f = open('%s\\%s' % (directory, filename), 'rt')
            for line in f:
                line = line.strip()
                starting.append(line)
            for ticker in first:
                if ticker not in starting:
                    first.remove(ticker)
    if first == []:
        print("There are no ticker symbols that are in all the lists.")
    else:
        first.sort()
        fn = open(time_stamp('common_stocks'), 'w')  # opens the new file with the date stamp
        for item in first:  # iterate through the list and append it to the list.
            fn.write(item)
            fn.write('\n')


file_name = input("Enter the file name:")  # ask for the file name.
common_stock(file_name)
