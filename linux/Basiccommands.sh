#Basic commands
#Show contents of the file.
  cat file.txt
#word count.
  wc file.txt
#sort contents of the file
  cat myfile.txt | sort
  cat myfile.txt | sort -r [sort in reverse order]
  # cut content of the file using delimeter [-d:] and show field 2 values
  cat myfile.txt | cut -d: -f2 | sort -r  


#pipe stderr values into file

ls myfile2222222.txt #this will throw error

ls myfile2222222.txt 2> myfileerror.txt # this will capture error message to a file

tail /etc/group
# Usage: tail [OPTION]... [FILE]...
#Pint the last 10 lines of each FILE to standard output.

diff
 # Compares 2 files or directories line by line
 # Several options for ignoring, filtering the comparison.
 # Output can be displayed in ed format. 
comm
 # Compare 2 sorted files line by line.
 # Output displayed in 2 columns.
cmp
 # Compare 2 files byte by byte and return the position of the first difference.


