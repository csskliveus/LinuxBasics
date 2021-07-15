# PID : unique number for each process

#* PID : primary key for processes
#* parent id : pid of process that started this one, if parent dies then child process is reparented to "init" process
#* UID : tells which user owns the process (same for groupID)
#* EffectiveUserID : (EUID) process spawned by user but shouldn't have same permissions as user (same for EgroupID)
#* Niceness : if NI high then it's low priority and let's lower NI processes take resources
