from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
	RUN_EVERY_MINS = 1 # every 2 hours
	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
	code = 'task'    # a unique code

	def do(self):
		print("Ah po workea!")