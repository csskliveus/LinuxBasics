useradd -m -d /home/linuxuser -s /bin/bash linuxuser
  # -m adds a new users with home directory [with -m as option].
  # -d home directory
  # shell as /bin/bash
  # -g , we can assign user to a group.
# set passwd for user 
passwd linuxuser

# Update user properties. For more properties use usermod --help 
usermod -U  [unlock the user account]
usermod -L [lock user account]

