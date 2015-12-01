#!/usr/bin/python

import json
import random
import sys

ss_names = None


def secret_santa(filename, output):
    names = get_ss_names(filename)
    options = len(names)  # Number of SS players
    list_remaining = range(options)  # Creates a list from [0, # of SS players)

    for i, n in enumerate(names):
        # Pick a random player
        assigned_num = random.choice(list_remaining)
        while (assigned_num == i):  # Make sure you don't assign to yourself
            assigned_num = random.choice(list_remaining)  # Pick new person
        n["assigned_to"] = names[assigned_num]["name"]  # Assign that person
        list_remaining.remove(assigned_num)  # Remove that so not picked again

    print_to_file(names, output)


def get_ss_names(filename):
    global ss_names
    if not ss_names:
        with open(filename) as f:
            ss_names = json.loads(f.read())

    return ss_names


def print_to_file(list, output):
    for person in list:
        email_string = ("Congrats {}! You have been assigned to {}."
                        " Their favorite color is {}. These are a few of their"
                        " favorite things: {}. Have fun being their Secret"
                        " Santa!").format(person["assigned_to"],
                                         person["name"],
                                         person["color"],
                                         person["likes"])
        with open(output, "a") as myfile:
            myfile.write(email_string + "\n\n")
        print email_string + "\n"
if __name__ == "__main__":
  secret_santa(sys.argv[1], sys.argv[2])
