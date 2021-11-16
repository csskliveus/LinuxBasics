# grep [Global Regular Expressions Print]

# ignore word case
grep -i "boo" /etc/passwd

#fgrep
# fgrep filter searches for fixed-character strings in a file or files.
# fgrep [options] pattern [files]

# grep recursively [searches for this IP across all the folders under etc]
grep -r "192.168.1.1" /etc/ 

# grep for searching words only
grep -w "boo" file

# Count lines that have word matching

grep -c 'word' /path/to/file
# https://www.cyberciti.biz/faq/howto-use-grep-command-in-linux-unix/ 
# https://swcarpentry.github.io/shell-novice/07-find/index.html
# Options	Description
# -i	Ignore case distinctions on Linux and Unix
# -w	Force PATTERN to match only whole words
# -v	Select non-matching lines
# -n	Print line number with output lines
# -h	Suppress the Unix file name prefix on output
# -r	Search directories recursivly on Linux
# -R	Just like -r but follow all symlinks
# -l	Print only names of FILEs with selected lines
# -c	Print only a count of selected lines per FILE
# --color	Display matched pattern in colors

# Regex
# ^ The start of a string or line.  grep '^The' <filename>
# $ The end of the string. 
# . wild card search can match any character. 
# | matches a specific characters or group of characters on either side. 
# \ Used to escape special character
# t the character t
# az the string "az"

grep -i '^u' /etc/passwd # search for lines which starts with 'u'. 

grep 'h$' /etc/passwd  # search for lines which ends with 'h'.

grep '^T[a-z][^e]' # line starts with T and doesnot ends with E.

#Look for all files in the current directory and in all of its subdirectories
# in Linux for the word ‘httpd’

 grep -R 'httpd' .

# AWK
  # An AWK program is made up of patterns and actions to be performed when a pattern match is found. 
  # It scans input lines sequentially and examines each one to determine whether it contains a pattern matching one specified by user.
