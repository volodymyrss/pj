#!/usr/bin/env python

import click
import sys
import json
import ast

@click.command()
def p2j():
    for l in sys.stdin.readlines():
        print(json.dumps(ast.literal_eval(l)))

#def 
#alias j2y='python -c "import sys,json,yaml; print(yaml.dump(json.loads(sys.stdin.read())))"'


if __name__ == "__main__":
    p2j()
