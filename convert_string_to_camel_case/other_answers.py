# Other answers:

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s


def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])


def to_camel_case(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)

def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])
