#!usr/bin/env python

from crontab import CronTab

def set_cronuser(user):
    my_cron = CronTab(user=user)
    return my_cron

def set_cron_job(cron, command, comment):    
    job = cron.new(command=command, comment=comment)
    return job

def set_cron_time(job,timename='minute',time=1):
    if timename.lower() == 'minute':
        job.minute.every(time)
    elif timename.lower() == 'hour':
        job.hour.every(time)
    else:
        print('timeframe not found!')

def update_cron(cron, identifier,timename='minute',time=1):
    for job in cron:
        if job.comment == identifier:
            set_cron_time(job, timename, time)


if __name__ == '__main__':
    """
    CRON =set_cronuser('fritz')
    ID = 'dateinfo'
    update_cron(CRON,ID,'hour',1)
    CRON.write()
    for item in CRON:
        print(item)
    """
    CRON = set_cronuser('fritz')
    COMMAND = 'python $HOME/printdatetime.py'
    COMMENT = 'dateinfo'
    JOB = set_cron_job(CRON, COMMAND, COMMENT)
    set_cron_time(JOB,'minute',10)
    set_cron_time(JOB,'hour',1)
    CRON.write()
    for item in CRON:
        print(item)
