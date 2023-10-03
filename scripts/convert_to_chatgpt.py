#!/usr/bin/env python

"""
Converts the PIsCo corpus into the ChatGPT message format.
"""

import sys
import os
import json


def convert_file(path):
    with open(path, "r") as f:
        lines = f.readlines()

    chat = []

    current_user = ""
    current_message = []

    def end_message():
        nonlocal current_message
        nonlocal current_user

        if not current_user:
            return

        m = "\n".join(current_message)
        chat.append({"role": current_user, "content": m})
        current_message = []
        current_user = ""

    def new_message(user):
        nonlocal current_user
        current_user = user

    for line in lines:
        if line == "<|user|>\n":
            end_message()
            new_message("user")
        elif line == "<|system|>\n":
            end_message()
            new_message("assistant")
        else:
            current_message.append(line.strip())

    end_message()

    return { "messages": chat }


def walk_dir(in_dir, out_file):
    out = open(out_file, "w")

    for root, dirs, files in os.walk(in_dir):
        for file in files:
            # if filename ends in .md
            if file.endswith(".md"):
                path = os.path.join(root, file)
                print(path)
                chat = convert_file(path)
                out.write(json.dumps(chat) + "\n")


if __name__ == "__main__":
    in_dir = sys.argv[1]
    out_file = sys.argv[2]
    walk_dir(in_dir, out_file)
