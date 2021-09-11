#!python3
"""Format pixels backup data for analysis.

index.html imports the data json as a <script> import. The data json must
therefore actually be a js script that stores the json in the variable 'data'.

Usage: python format-data.py /path/to/pixels.json
"""
import os
import sys

default_input = "/tmp/pixels_decrypted.json"
input_filename = sys.argv[1] if len(sys.argv) > 1 else default_input
# save to current directory as data.json
output_filename = os.path.join(os.path.dirname(sys.argv[0]), "data.json")

with open(input_filename, "r") as file:
    pixels = file.read()

# escape interfering characters (as requested in the README)
pixels = pixels.replace("\\", "\\\\")
pixels = pixels.replace("'", "\\'")

with open(output_filename, "w") as file:
    file.write("data='" + pixels + "'")
