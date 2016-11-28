"""
Generate text using Markov Chain model based on dictionary of n-grams

:args f: Path to file containing transition frequencies
:args s: Optional seed for getting started
:args l: Output length, num characters
:output: text file containing generated text

"""


import json
import argparse
from random import choice
import re
import os

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", help="Path to file containing transition frequencies.")
    parser.add_argument(
        "-s", "--seed", help="Optional seed for getting started.")
    parser.add_argument(
        "-l", "--length", help="Output length in characters.")
    args = parser.parse_args()

    file_name = args.file
    seed = args.seed
    length = int(args.length)

    with open(file_name, "r") as f:
        transitions = json.load(f)

    if seed:
        output = seed
    else:
        output = transitions['']

    fname = re.findall(r'(.+).json', os.path.split(file_name)[1])[0]
    num_chars = int(re.findall(r'_(\d+)', fname)[0])

    while True:
        current_char = output[-num_chars:]
        next_char = choice(transitions[current_char])
        output += next_char

        if len(output) >= length:
            break

    out_name = "{}_output.txt".format(fname, length)

    with open(out_name, "w") as f:
        f.write(output)
