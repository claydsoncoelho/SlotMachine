# SlotMachine

This program simulates a slot machine functionality. It consists of 3 parts:

1 - A configuration file
2 - A model python code
3 - A view python code


1 - The configuration file is a csv file with 3 columns:

A - Symbol - A single symbol that can be visualized in a single wheel of the slot machine in a specific time. A wheel of a slot machine is made of many symbols printed on it. The wheel then spins and eventually stops showing one single symbol. Example: A, B, C, 1, 2, 3…

B - Chance - How many Symbols will be printed on the wheel of the slot machine. The bigger the number the higher the probability of the wheel, after spinning, stop in that Symbol. Example: If Symbol is A and Chance is 3, it means that each wheel will have A printed 3 times.

C – Prize – It’s an integer number that represents the multiplier of the bet in case the user won that round. Ex: If all the wheels stopped at Symbol A, then the user won that round. The value that they won is calculated by: Prize x Bet. So, if Prize is 3 and the user bet is $10, they won 3 x $10 = $30.


2 – The model is a fully operational slot machine. It is composed of 2 main classes:

	A – Class Wheel – A class that represents a single wheel. 
		Attributes:
			1 – symbol_list: The list of symbols printed on the wheel.
			2 – symbol_prize: A dictionary with a pair Symbol: Prize. In other words, what is the Prize of each Symbol.
			3 – current_symbol: Which Symbol from the symbol_list is showing now in the display of the that specific wheel.
		Methods:
			1 – spin(): This method spins the wheel, which will randomly pic another value from the symbol_list and show it in current_symbol.

	B – Class SlotMachine – A class that represent a fully functional slot machine.
		Attributes:
			1 – initial_balance: How much money the user deposited in the machine.
			2 – current_balance: How much money the user has inside the machine.
			3 – wheels: A list of 3 Wheels objects described above.
			4 – wheels_state: A list of 3 current_symbols of the 3 wheels.
			5 – prize: How much money the user won as a prize. It’s 0 if the user didn’t win on that round.
			6 – bet: How much money the user bet on that round.
7 – performance: A percentage representing how much money the user is gaining or losing compared to their initial_balance. The formula is: (current_balance - initial_balance) / initial_balance * 100.
		Methods:
			1 – play(): This method spins all the 3 wheels of the slot machine, get the new current_symbol of each wheel and save them in wheels_state attribute.

3 – The view is an interface that the user will interact to play the game. The interface could be Web, command line, graphical… The program is modular, so different interfaces can import and use the same model python code.
