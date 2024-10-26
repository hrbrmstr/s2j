import sys
import json
from idstools import rule

def main() -> None:
    if len(sys.argv) < 2:
        input_stream = sys.stdin
    else:
        input_stream = open(sys.argv[1], 'r')

    # Process each rule
    rules = []
    for r in rule.parse_fileobj(input_stream):
      rules.append(r)

    # Output JSON to stdout
    print(json.dumps(rules))

    # Close file if we opened one
    if input_stream is not sys.stdin:
        input_stream.close()
