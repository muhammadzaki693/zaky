import rich
import time
from rich.console import Console
from rich.table import Table
from rich.progress import track

class Text:
	def table(headers, rows):
		console = Console()
		table = Table(show_header=True)
		for header in headers:
			table.add_column(header)
		table.add_rows(*rows)
		console.log(table)
	
	def status(msg_wk, msg_com, tasks):
		console = Console()
		with console.status(msg_wk):
			while tasks:
			  task = tasks.pop(0)
			  time.sleep(1)
		  	console.log(task + " " + msg_com)
	
	def progress_bar(total, speed):
		for step in track(range(total)):
			time.sleep(speed)
			i = step