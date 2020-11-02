from cell import Cell
from random import randint

class Board:
	def __init__(self, rows, columns):
		self._rows = rows
		self._columns = columns
		self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

		self._generate_board()

	def draw_board(self):
		print('\n'*10)
		print('printing board')
		for row in self._grid:
			for column in row:
				print(column.get_print_character(), end='')
			print() # to create a new line 

	def _generate_board(self):
		for row in self._grid:
			for column in row:
				# there is a 33% chance cells spawn alive
				chance_number = randint(0, 2)
				if chance_number == 1:
					column.set_alive()

	def check_neighbour(self, check_row, check_column):
		# how deep the search is:
		search_min = -1
		search_max = 2

		# empty list to append neighbours into
		neighbour_list = []
		for row in range(search_min, search_max):
			for column in range(search_min, search_max):
				neighbour_row = check_row + row
				neighbour_column = check_column + column

				valid_neighbour = True

				# neighbour equals check cell
				if (neighbour_row) == check_row and (neighbour_column) == check_column:
					valid_neighbour = False

				# neighbour row out of range
				if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
					valid_neighbour = False

				# neighbour column out of range
				if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
					valid_neighbour = False

				if valid_neighbour:
					neighbour_list.append(self._grid[neighbour_row][neighbour_column])

		return neighbour_list

	def update_board(self):
		print('updating board')
		# cells list for living cells to kill and cells to resurrect or keep alive
		goes_alive = []
		gets_killed = []

		for row in range(len(self._grid)):
			for column in range(len(self._grid[row])):

				# check neighbours
				check_neighbour = self.check_neighbour(row, column)

				living_neighbours_count = []

				for neighbour_cell in check_neighbour:
					# check live status for neighbour_cell
					if neighbour_cell.is_alive():
						living_neighbours_count.append(neighbour_cell)

				cell_object = self._grid[row][column]
				status_main_cell = cell_object.is_alive()

				# if cell is alive, check neighbour status
				if status_main_cell == True:
					if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
						gets_killed.append(cell_object)

					if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
						goes_alive.append(cell_object)

				# else cell is dead
				else:
					if len(living_neighbours_count) == 3:
						goes_alive.append(cell_object)

		# set cell statuses
		for cell_items in goes_alive:
			cell_items.set_alive()

		for cell_items in gets_killed:
			cell_items.set_dead()