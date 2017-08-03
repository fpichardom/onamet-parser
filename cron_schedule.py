#!usr/bin/env python

from crontab import CronTab

class CronManager:
    def __init__(self):
        self.cron = CronTab(user=True)
    def hour_offset(self, command, offset=10, comment=None):
        cron_job = self.cron.new(command=command, comment=comment)
        cron_job.minute.on(offset)
        cron_job.hour.during(0, 23)
        self.cron.write()
        for job in self.cron:
            print(job)

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
    CRONIS = CronManager()
    COMMAND = 'python $HOME/python-apps/onamet-parser/onamet_24table.py'
    CRONIS.hour_offset(COMMAD, comment="onamet24h")
