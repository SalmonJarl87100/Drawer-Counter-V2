from tkinter import *
from tkinter.ttk import *


class ScrollFrame:
	def __init__(
		self, 
		parent, 
		canvasWidth=570, 
		canvasHeight=570, 
		yScroll=True, 
		xScroll=True
	):

		# defines master container
		self.body = Frame(parent)

		self.xBar = Scrollbar(self.body, orient="horizontal")
		self.yBar = Scrollbar(self.body)

		canvasWidth -= self.yBar.winfo_reqwidth()
		canvasHeight -= self.xBar.winfo_reqheight() + 100

		# creates a canvas to use for scrolling
		self.scrollingCanvas = Canvas(self.body, width=canvasWidth, height=canvasHeight)
		self.scrollingCanvas.grid(column=0, row=0)

		self.widgetFrame = Frame(self.scrollingCanvas)  # the frame in which widgets should be placed
		self.widgetFrame.bind(  # this updates the canvas to represent the proper dimensions when widgets are added to it
			"<Configure>", 
			lambda e: self.scrollingCanvas.configure(
				scrollregion=self.scrollingCanvas.bbox("all")
			)
		)

		# this is what allows the child frame to scroll
		self.scrollingCanvas.create_window(
			(0, 0),
			window=self.widgetFrame,
			anchor="nw",
			width=canvasWidth,
			height=canvasHeight)

		# creates and binds the x and y scroll bars
		self.xBar.config(command=self.scrollingCanvas.xview)
		self.yBar.config(command=self.scrollingCanvas.yview)
		self.scrollingCanvas.config(xscrollcommand=self.xBar.set, yscrollcommand=self.yBar.set)

		# grids the scroll bars based on if the user needs either of them
		if xScroll:
			self.xBar.grid(column=0, row=1, sticky="new")
		
		if yScroll:
			self.yBar.grid(column=1, row=0, sticky="nes")
			

if __name__ == "__main__":
	root = Tk()
	
	mainFrame = ScrollFrame(root, xScroll=True)
	
	for x in range(50):
		lbl = Label(mainFrame.widgetFrame, text="Tests")
		lbl.grid(column=x, row=x)
	
	mainFrame.body.grid()
	
	root.mainloop()
