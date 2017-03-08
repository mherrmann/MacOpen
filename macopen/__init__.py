from fman import DirectoryPaneCommand
from subprocess import Popen

class MacOpen(DirectoryPaneCommand):
	def __call__(self):
		file_under_cursor = self.pane.get_file_under_cursor()
		if file_under_cursor:
			Popen('open "%s"' % file_under_cursor, shell=True)