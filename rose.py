#!/usr/bin/env python3

import re

import pprint

DFLT_FLAGS = {
        'version': '0.4',
        'tags': set(),
        'inline-branch': '\t',
        'preferred-indent': '\t'
        }

FLAG_ORDER = ['preferred-indent', 'inline-branch']

def parse_flag(text):
    if re.match(r'^[A-z]+=.+', text):
        partition = text.index('=')
        return {
                'action': 'set',
                'key': text[:partition],
                'value': text[partition + 1:]
                }
    else:
        return {'action': 'tag', 'content': text}

def load_meta(line):
    no_flower = line[3:]
    flags_text = no_flower.strip()
    flags = [parse_flag(f) for f in flags_text.split('\t')]
    flagstate = DFLT_FLAGS
    for flag in flags:
        if flag['action'] == 'set':
            flagstate[flag['key']] = [flag['value']]
        else:
            flagstate['tags'].add(flag['content'])
    return flagstate

def rose_header(line):
    return re.match(r'^-[-+]@', line)

def get_indent(line):
    indent = 0
    while line[indent].isspace():
        indent += 1
    return indent

def is_blank(line):
    return re.search(r'\S', line) is None

def load_line(line, line_number=None):
    indent = get_indent(line)
    main, *inline_children = line[indent:].split('\t')
    node = {
        'content': main,
        'indent': indent,
        'line': line_number,
        'zoom': []
        }
    for child in inline_children:
        node['zoom'].append({
            'content': child,
            'indent': float('inf'),
            'line': line_number,
            'zoom': []
            })
    return node

def load_body(lines):
    root = {
        'content': '',
        'indent': -1,
        'line': -1,
        'zoom': []
        }
    for i, line in enumerate(lines):
        if is_blank(line):
            continue
        node = load_line(line, i)
        parent = root
        while (
                parent['zoom']
                and parent['zoom'][-1]['indent'] < node['indent']
                ):
            parent = parent['zoom'][-1]
        parent['zoom'].append(node)
    return root

def load_tree(lines):
    if rose_header(lines[0]):
        metadata = load_meta(lines[0])
        lines = lines[1:]
    else:
        metadata = {}
    root = load_body(lines)
    root['meta'] = metadata
    return root

def loads(text):
    return load_tree(text.split('\n'))

def load(addr):
    with open(addr, 'r') as f:
        return loads(f.read())

def dumps(root, flags={}):
    flag_strs = [f + '=' + repr(flags[f]) for f in FLAG_ORDER if f in flags]
    if flag_strs:
        header = '-+@\t' + '\t'.join(flag_strs) + '\n\n'
    else:
        header = ''
    flags = {**DFLT_FLAGS, **flags}
    out_lines = []
    def subtree(node, depth=0):
        indentation = flags['preferred-indent'] * depth
        content = node['content']
        out_lines.append(indentation + content)
        for child in node['zoom']:
            subtree(child, depth=depth+1)
    for child in root['zoom']:
        subtree(child)
    return header + '\n'.join(out_lines)

def dump(data, addr):
    with open(addr, 'w') as f:
        f.write(dumps(data))

def query(key, template):
    pass

if __name__ == '__main__':
    node_tree = loads('a\tb\tc\td')
    pprint.pprint(node_tree)
    print(dumps(node_tree))
