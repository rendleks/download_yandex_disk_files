import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    target_file = args.path
    
    return os.path.abspath(target_file)


def main():
    parse_args()


if __name__ == "__main__":
    main()