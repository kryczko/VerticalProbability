#!/usr/bin/env python

import os, sys, numpy


ilength = int(sys.argv[1]) # Input how many bins you would like.

i = numpy.zeros(ilength, dtype = int) # Empty array with length = number of bins.

nbin = sys.argv[1] # Input how many bins you would like.

zmax = 60

zmin = 0

binsize = float((zmax - zmin))/float(nbin) # The length of each bin. 

f = open('new.xyz', 'r') # Defining what file to run the program on.

def main():
    
    zcoordinates = [] 
    total_oxygen_atoms = 0	
    for line in f.readlines(): # For statement to read each line.
        if len(line.split()[:]) == 4 and line.split()[0] == 'O': # If statement to 
	    g = float(line.split()[3])                           # to extract the  
            zcoordinates.append(g)                             # Oxygen atom data.
	    total_oxygen_atoms += 1                           
        	      
    for value in zcoordinates:    # Loop to place the z-coordinates in the appropriate bin.
        bin_number = int(value/binsize)
	i[bin_number] += 1
        
    z_values = []           # new list of the z-values
    m = -binsize
    n = 0
    z_axis = []		# list of numbers along z-axis	
    for number in i:
	m += binsize
	n += binsize
	z_axis.append(m)
	z_axis.append(n)
	z_values.append(number)
	z_values.append(number)	

    zipped = zip(z_axis, z_values)   # Creates a list of tuples 
    datafile = open('oxygen_atoms_data.dat', 'w')
    datafile.write("%s %s\n\n" %('# z-axis', '# probability'))	
    for line in zipped:
	z = line[0]
	percent = float(line[1])/total_oxygen_atoms
	datafile.write("%f %f\n" % (z,percent))  # Writes the data to a file

if __name__ == '__main__':
    main()
