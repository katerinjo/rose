import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from rose import *

import pprint

family = '''grandparent
\tparent
\t\tsibling
\t\t\tnibling
\t\ttarget
\t\t\tchild
\t\t\t\tgrandchild
\t\tbrother
\t\t\tnephew
\t\tsister
\t\t\tniece
\taunt
\tuncle
\tommer
\t\tcousin
'''

family_tree = {
    'content': '',
     'indent': -1,
     'line': -1,
     'zoom': [{'content': 'grandparent',
               'indent': 0,
               'line': 0,
               'zoom': [{'content': 'parent',
                         'indent': 1,
                         'line': 1,
                         'zoom': [{'content': 'sibling',
                                   'indent': 2,
                                   'line': 2,
                                   'zoom': [{'content': 'nibling',
                                             'indent': 3,
                                             'line': 3,
                                             'zoom': []}]},
                                  {'content': 'target',
                                   'indent': 2,
                                   'line': 4,
                                   'zoom': [{'content': 'child',
                                             'indent': 3,
                                             'line': 5,
                                             'zoom': [{'content': 'grandchild',
                                                       'indent': 4,
                                                       'line': 6,
                                                       'zoom': []}]}]},
                                  {'content': 'brother',
                                   'indent': 2,
                                   'line': 7,
                                   'zoom': [{'content': 'nephew',
                                             'indent': 3,
                                             'line': 8,
                                             'zoom': []}]},
                                  {'content': 'sister',
                                   'indent': 2,
                                   'line': 9,
                                   'zoom': [{'content': 'niece',
                                             'indent': 3,
                                             'line': 10,
                                             'zoom': []}]}]},
                        {'content': 'aunt', 'indent': 1, 'line': 11, 'zoom': []},
                        {'content': 'uncle', 'indent': 1, 'line': 12, 'zoom': []},
                        {'content': 'ommer',
                         'indent': 1,
                         'line': 13,
                         'zoom': [{'content': 'cousin',
                                   'indent': 2,
                                   'line': 14,
                                   'zoom': []}]}]}]}

autodescriptive = '''first root\tinline one\tinline two
\tindented\tindented line one\tindented line two
'''

def equals(a, b):
    if type(a) == list and type(b) == list:
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not equals(a[i], b[i]):
                return False
        return True
    elif type(a) == dict and type(b) == dict:
        if len(a) != len(b):
            return False
        for key in a:
            if not equals(a[key], b[key]):
                return False
        return True
    else:
        return a == b

def matches(subject, test):
    if type(subject) == list and type(test) == list:
        for i in range(len(test)):
            if len(subject) <= i or not equals(subject[i], test[i]):
                return False
        return True
    elif type(subject) == dict and type(test) == dict:
        for key in test:
            if not key in subject or not equals(subject[key], test[key]):
                return False
        return True
    else:
        return a == b

def body_equal(a, b):
    if a.startswith('-+@') or a.startswith('--@'):
        a = a[a.index('\n') + 1:]
    if b.startswith('-+@') or b.startswith('--@'):
        b = b[b.index('\n') + 1:]
    return a.strip() == b.strip()

def test(was_successful, test_name, fun_input, fun_output):
    if was_successful:
        print('✓', test_name)
    else:
        print('FAILED', message)
        print('---')
        pp.pprint(fun_input)
        print('>>>')
        pprint.pprint(fun_output)
        print('...')

load_family = loads(family)
dump_family = dumps(load_family)

test(matches(load_family, family_tree), 'LOAD FAMILY', family, load_family)
test(body_equal(dump_family, family), 'DUMP FAMILY', family_tree, dump_family)
