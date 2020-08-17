# Handling Date
from datetime import datetime
from django.utils import timezone

# Read .ics file and return list of reservation
def read_calendar(calendar_lines):
	print("<< read_calendar >>")
	# Split and keep only the Event (do not care about the rest)
	calendar_lines = calendar_lines.split("\n")
	print(calendar_lines)
	event_blocks = []
	has_event = False
	for line in calendar_lines:
		if line == "BEGIN:VEVENT":
			event_blocks.append(list())
			has_event = True
		elif line == "END:VEVENT":
			has_event = False

		if has_event:
			event_blocks[-1].append(line)
	print("\n\n")
	# Create the event object
	events = list()
	for event_block in event_blocks:
		events.append(dict())
		last_append = ""
		for line in event_block:
			if line.startswith("DTEND"):
				date_str = line[line.find("DATE:")+len("DATE:"):]
				events[-1]['end_date'] = datetime.strptime(date_str, "%Y%m%d")
				last_append = "end_date"

			elif line.startswith("DTSTART"):
				date_str = line[line.find("DATE:")+len("DATE:"):]
				events[-1]['start_date'] = datetime.strptime(date_str, "%Y%m%d")
				last_append = "start_date"

			elif line.startswith("UID"):
				events[-1]['uid'] = line[line.find("UID:")+len("UID:"):]
				last_append = "uid"

			elif line.startswith("DESCRIPTION"):
				events[-1]['description'] = line[line.find("DESCRIPTION:")+len("DESCRIPTION:"):]
				last_append = "description"

			if len(last_append) > 0 and (line.startswith(" ") or line.startswith("\t")):
				events[-1][last_append] += line[1:]

	print(events)