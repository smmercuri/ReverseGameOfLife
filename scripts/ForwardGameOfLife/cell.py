class Cell:
	def __init__(self):
		'''
		Class holding init status of the cell (dead).
		Ability to set and fetch new statuses with methods
		'''
		self._status = 'Dead'

	def set_dead(self):
		'''
		method sets cell status to dead
		'''
		self._status = 'Dead'

	def set_alive(self):
		'''
		method sets cell status to alive
		'''
		self._status = 'Alive'

	def is_alive(self):
		'''
		method checks if cell is Alive
		returns True if it is alive, False if not
		'''
		if self._status == 'Alive':
			return True
		return False

	def get_print_character(self):
		'''
		method returning a status character of our choice to print on the board
		'''
		if self.is_alive():
			return '0'
		return '*'