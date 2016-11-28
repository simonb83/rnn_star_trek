"""
Generate dictionary of character or bi-gram pairs for Markov Chain text generation

:flags f: Path to file containing training text
:flags l: Number of characters to use
:output: Dictionary of pairs as json file

"""

import json
import argparse
import re
import os


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--file", help="Path to file containing training text.")
    parser.add_argument(
        "-l", "--length", help="Number of characters to use.")
    args = parser.parse_args()

    file_name = args.file
    length = int(args.length)

    with open(file_name, "r") as f:
        input_text = f.read()

    transitions = {}
    transitions[''] = input_text[:length]

    for i in range(0, len(input_text) - length):
        key = input_text[i: i + length]
        val = input_text[i + length: i + length + length]
        if key in transitions:
            transitions[key].append(val)
        else:
            transitions[key] = [val]

    transitions[input_text[-length:]] = input_text[:length]

    fname = re.findall(r'(.+).txt', os.path.split(file_name)[1])[0]
    out_name = "{}_markov_{}.json".format(fname, length)

    with open(out_name, "w") as f:
        json.dump(transitions, f)
