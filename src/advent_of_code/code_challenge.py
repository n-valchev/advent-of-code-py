import argparse
import importlib
import os

parser = argparse.ArgumentParser(
    prog="Run Code Challenge",
    description="This is the entry point for code challenge solutions.",
    epilog="./code_challenge.py <the_name_of_the_module> - expects input.txt file located in the module containing the input of the challenge",
)

parser.add_argument("code_challenge_filename")

def run():
    args = parser.parse_args()

    code_challenge_module = importlib.import_module(f"advent_of_code.{args.code_challenge_filename}")

    input_reader = open(f"{os.path.dirname(code_challenge_module.__file__)}/input.txt", "r")

    code_challenge_module.run(input_reader)
