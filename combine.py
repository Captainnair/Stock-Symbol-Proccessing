import os  # import os so we can access the directory
import datetime  # need datetime for the time stamp


combine = []


def time_stamp(name, fmt='{name}_%m-%d-%y.txt'):  # creates the time stamp for the program.
    return datetime.datetime.now().strftime(fmt).format(name=name)


def combine_list(directory):
    time = datetime.datetime.now()  # creating the time from the time_stamp program.
    time = time.strftime("%m-%d-%y")
    for filename in os.listdir(directory):  # goes through the file names in the directory
        if filename.endswith(".txt"):   # finds which files end with txt
            f = open('%s\\%s' % (directory, filename), 'rt')  # opens files and does not hard code what the value is
            for line in f:
                line = line.strip()  # strips off the values that come with the string so it is just the stock numbers
                if line not in combine:  # checks if the value is in the list, if not then add it to the string
                    combine.append(line)
                else:
                    nothing = 0
        else:
            continue  # if the filename doesn't end with txt then that means to continue to the next value
    combine.sort()  # sort the file in alphabetical order.
    fn = open(time_stamp('combined'), 'w')  # opens the new file with the date stamp
    for item in combine:  # iterate through the list and append it to the list.
        fn.write(item)
        fn.write('\n')


file_name = input("Enter the file name:")  # ask for the file name.
combine_list(file_name)
