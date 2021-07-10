#!python3
# for use in combination with peterbot
# github.com/plojyon/peter
import os
import sys

input_filename = "/tmp/pixels_decrypted.json";
output_filename = os.path.join(os.path.dirname(sys.argv[0]), "data.json");

with open(input_filename, "r") as file:
	pixels = file.read();

# replace as requested in the README
pixels = pixels.replace('\\', '\\\\');
pixels = pixels.replace("'", "\\'");

with open(output_filename, "w") as file:
	file.write("data='"+pixels+"'");
