#!/usr/bin/python3
# A function that returns the JSON
# representation of an object (string)
"""define to_json_strin function.
   import json.
"""

import json


def to_json_string(my_obj):
    """returns JSON representation of an object(string)."""

    return json.dumps(my_obj)
