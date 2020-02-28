import xml.etree.ElementTree as ET
import argparse
import os.path
#from os import path

def main():
	parser = argparse.ArgumentParser(description='Converts a Renesas sfrx file to svd format for use in eclipse')
	parser.add_argument('-i', metavar='FILE', help='The file to be converted')
	#parser.add_argument('--output_file', metavar='FILE', help='an integer for the accumulator')
	args = parser.parse_args()

	assert os.path.exists(args.i)
	tree = ET.parse(args.i)
	root = tree.getroot()

	for child in root:
		if child.tag == "header":
			header_in = child
		elif child.tag == "moduletable":
			registers_in = child

	for child in header_in:
		print(child)
	print(registers)

	#Create the sections of the out file
	'''
	<device>
		<vendor></vendor>
		<vendorID></vendorID>
		<name></name>
		<version></version>
		<series></series>
		<addressUnitBits></addressUnitBits>
		<width></width>
		<size></size>
		<description></description>
		<licenseText></licenseText>
		<cpu>
			<name>CM3</name>
			<revision>r2p1</revision>
			<endian>little</endian>
			<mpuPresent>False</mpuPresent>
			<fpuPresent>False</fpuPresent>
			<fpuDP>False</fpuDP>
			<nvicPrioBits>3</nvicPrioBits>
			<vendorSystickConfig>False</vendorSystickConfig>
		</cpu>
	</device>
	'''
	device = ET.Element("device")  #This is the parent(is that what it's called?) of the entire xml file

	return 0

if __name__== "__main__" :
	main()