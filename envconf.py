import re


def parse(src):
    NEWLINE = "\n"
    RE_INI_KEY_VAL = r"^\s*([\w.-]+)\s*=\s*(.*)?\s*$"
    RE_NEWLINES = r"\n"
    NEWLINES_MATCH = r"\n|\r|\r\n"

    obj = {}

    lines = re.split(NEWLINES_MATCH, src, flags=re.MULTILINE)

    for idx, line in enumerate(lines):
        keyValueArr = re.match(RE_INI_KEY_VAL, line)

        if keyValueArr is None:
            continue

        key, val = keyValueArr.groups()

        isDoubleQuoted = val[0] == '"' and val[-1] == '"'
        isSingleQuoted = val[0] == "'" and val[-1] == "'"

        if isDoubleQuoted:
            val = val[1:-1]
            val = val.strip()

        if val == "true" or val == "false":
            val = val == "true"
        elif val.isdigit():
            val = int(val)
        elif val.count(".") == 1 and val.replace(".", "").isdigit():
            val = float(val)

        if isSingleQuoted:
            val = val[1:-1]
            val = val.strip()

        obj[key] = val

    return obj


def env(filename="env.conf"):

    with open(filename, encoding="utf8") as fp:
        parsed = parse(fp.read())
    return parsed


def get(key, val=None, filename="env.conf"):
    data = env(filename=filename)
    return data.get(key, val)


if __name__ == "__main__":

    print(env())
