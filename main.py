from flet import *
from store import root_model
from mopyx import model,render,render_call,action



def main(page:Page):
	page.window_width = 300

	# AND NOW YOU CAN USE render_call FOR RENDER UI
	counter = Text(root_model.counter,size=50,weight="bold")



	# AND FOR CHANGE STATE counter YOU MUST CALL ACTION
	@action
	def addnew(e):
		counter.value += 1
		print(counter.value)
		page.update()

	@action
	def decnew(e):
		counter.value -= 1
		print(counter.value)
		page.update()

	@render
	def you_ui_render_here():
		return Row([
			ElevatedButton("add",
			bgcolor="green",color="white",
			on_click=addnew

				),
			counter,
			ElevatedButton("incrment",
			bgcolor="red",color="white",
			on_click=decnew

				),
			])



	page.add(
		Column([
		Text("Mobx State manager",size=30),
		render_call(you_ui_render_here)
			])
		)

flet.app(target=main)
