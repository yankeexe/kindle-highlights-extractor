import sys
import json
import argparse
from itertools import zip_longest
from collections import defaultdict


def init_argparse():
    """
    Initialize argparse module for commandline argument parsing.
    """
    parser = argparse.ArgumentParser(
        description="Manage Kindle Clippings.", epilog="Happy Reading  :)",
    )

    parser.add_argument("filename", type=str, help="Path to `My Clipping.txt` file.")
    parser.add_argument("-o", "--output", help="Output JSON file name")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def clippings_jsonify(args):
    """
    Takes the file input and process it.
    """
    data_dict = defaultdict(list)
    filename = args.filename
    output_filename = args.output or "clippings"

    with open(filename, "r", encoding="utf-8-sig") as txt:
        for item in zip_longest(*[iter(txt)] * 5, fillvalue=""):
            strings = " ".join(item)
            lists = list(strings.split("\n"))

            book_name = lists[0].encode("ascii", "ignore").decode("utf-8")
            clipping = lists[3].encode("ascii", "ignore").decode("utf-8").lstrip()

            # Check for empty string
            if clipping:
                data_dict[book_name].append(clipping)

    # Remove duplicate values
    for key, value in data_dict.items():
        data_dict[key] = list(set(value))

    # Output JSON file.
    with open(f"{output_filename}.json", "w+") as f:
        json.dump(dict(data_dict), f, indent=4)

    print(f"Clippings JSON File: {output_filename}.json")


if __name__ == "__main__":
    args = init_argparse()
    clippings_jsonify(args)
