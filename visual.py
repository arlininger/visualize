#!/usr/bin/python

''' visualize

Usage:
	visualize.py --input=ifile --output=ofile

Options:
	-h --help	Show this screen.
	--input=ifile	Input File
	--output=ofile	Output File
'''

from docopt import docopt
import Image

import pdb

def increment((x,y,z)):
	try:
		z = z + 1
	except IndexError:
		z = 0;
		try:
			y = y + 1
		except IndexError:
			y = 0;
			try:
				x = x + 1
			except IndexError:
				x = 255
				y = 255
				z = 255
	return (x,y,z)
	
def reader(myfile):
	while True:
		chunk = myfile.read(1)
		if chunk:
			yield chunk
		else:
			return

def main(arg):
	
	infile = open(arg['--input'],'rb')
	img = Image.new( 'RGB', (256,256), "black")
	pixels = img.load()
	last = infile.read(1)
	last = ord(last)
	#pdb.set_trace()
	for x in reader(infile):
		y = ord(x)
		pixels[last,y] = increment(pixels[last,y])
		last = y

	img.save(arg['--output'])	
	infile.close()


if __name__ == "__main__":
	arg = docopt(__doc__)
	main(arg)
