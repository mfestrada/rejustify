import argparse
from .justify import justify

def main():
    parser = argparse.ArgumentParser(
        description='justifies given text to a given pagewidth', 
        usage='rejustify --pagewidth 20 --text "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi auctor congue nibh id aliquam."')
    parser.add_argument('--pagewidth', metavar='WIDTH', type=int, help='width of page', required=True)
    parser.add_argument('--text', type=str, help='text to justify, must be wrapped in quotes ""', required=True)
    args = parser.parse_args()

    answer = justify(args.text, args.pagewidth)
    
    for i, line in enumerate(answer):
        print('Array [{}] = "{}"'.format(i + 1, line))

if __name__ == '__main__':
    main()
