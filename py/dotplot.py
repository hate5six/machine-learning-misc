import Image
import string
import sys
import os
import hashlib
from glob import glob

exclude = set(string.punctuation)

# Token to unique rgb hashing
def color_hash(sequence):
	tokens = list(set(sequence))
	colormap = {}
	for token in tokens:
		hashed = hashlib.sha224(token).hexdigest()
		r,g,b = hashed[:2], hashed[2:4], hashed[4:6]
		colormap[token] = (int(r,16), int(g, 16), int(b, 16))
	return colormap

# Simple tokenizer. Removes punctuation, lowercases and splits on whitespace
def read_file(fname):
	f = open(fname)
	stream = f.read()
	return ''.join(c for c in stream if c not in exclude).lower().split()

# Produces an NxN dotplot of a sequence against itself
def generate_dp(sequence, outpath):
	N = len(sequence)
	colormap = color_hash(sequence)
	img = Image.new("RGB", (N, N), "white")
	pixels = img.load()

	for i in range(N):
		for j in range(N):
			if sequence[i]==sequence[j]:
				pixels[i, N-j-1] = colormap[sequence[i]]
	img.save(outpath+".png")

# Batch run over all text files in an input directory
def run():
	files = glob(os.path.join(sys.argv[1], "*.txt"))
	for f in files:
		sequence = read_file(f)
		outpath = f.split('.')[0]
		generate_dp(sequence, outpath)

if __name__ == '__main__':
	run()
