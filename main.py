import argparse
import sys
from engine import TreeBuilder

def main():
    parser = argparse.ArgumentParser(description='Visualize tree structure from flat input.')
    parser.add_argument('--input', required=True, help='Comma separated pairs, semicolon delimited (e.g. A,B;B,C)')
    
    args = parser.parse_args()
    try:
        pairs = [tuple(pair.split(',')) for pair in args.input.split(';')]
        builder = TreeBuilder(pairs)
        for root in builder.roots:
            print(builder.render(root))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()