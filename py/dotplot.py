import Image
import string
import sys
from glob import glob

exclude = set(string.punctuation)

# Simple tokenizer. Removes punctuation, lowercases and splits on whitespace
def read_file(fname):
	f = open(fname)
	stream = f.read()
	return ''.join(c for c in stream if c not in exclude).lower().split()

# Produces an NxN dotplot of a sequence against itself
def generate_dp(sequence, outpath):
	N = len(sequence)
	img = Image.new("RGB", (N, N), "white")
	pixels = img.load()

	for i in range(N):
		for j in range(N):
			if sequence[i]==sequence[j]:
				pixels[i, N-j-1] = (0, 0, 0)
	img.save(outpath+".png")

# Batch run over all text files in an input directory
def run():
	files = glob("%s\\*" % sys.argv[1])
	for f in files:
		sequence = read_file(f)
		outpath = f.split('.')[0]
		generate_dp(sequence, outpath)

if __name__ == '__main__':
	run()