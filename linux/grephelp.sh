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
