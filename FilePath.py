from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import Tk
import json

class Path:
	def path_window(self):
		root = Tk()
		root.withdraw()
		self.PathSave = askdirectory()
		root.destroy()
		return self.PathSave

	def read_json(self):
		with open('data_file.json', 'r') as FileJson:
			self.FileRead = json.load(FileJson)
		return self.FileRead

	def get_list_info(self, Number = 1):
		Pattern = self.FileRead[Number]
		self.NameProject = Pattern["NameProject"]
		self.Name = Pattern['Name']
		self.Angle = Pattern['Angle']
		self.Length = Pattern['Length']
		self.Width = Pattern['Width']