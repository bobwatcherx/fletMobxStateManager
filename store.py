# NOW CREATE STORE COUNTER
from mopyx import model,render,render_call,action

@model
class MyModel:
	def __init__(self):
		self.counter = 0

root_model = MyModel()
