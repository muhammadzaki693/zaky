import maths
import sorting
import usl
import func
import types
import rich
from rich import *
from func import *

def init():
	Text.status("installing rich module","complete", ["install pretty", "install traceback"])
	traceback.install()
	pretty.install()