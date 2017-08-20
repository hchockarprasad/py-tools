# Common Utils form BMAN helper

import re

def gen_val_str(value):
    # Remove REGEX
    result = re.sub('[^a-zA-Z0-9]', '', value)
    # Remove white spaces and convert to lower-case
    result = "".join(result.lower().split())
    return result
