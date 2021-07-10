#!python3
# for use in combination with peterbot
# github.com/plojyon/peter

with open("/tmp/pixels_decrypted.json", "r") as file:
	pixels = file.read();

pixels = pixels.replace('\\', '\\\\');
pixels = pixels.replace("'", "\\'");
with open("data.json", "w") as file:
	file.write("data='"+pixels+"'");
