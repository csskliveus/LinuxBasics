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