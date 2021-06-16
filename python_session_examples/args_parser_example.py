import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--file', default='some value',
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.file)