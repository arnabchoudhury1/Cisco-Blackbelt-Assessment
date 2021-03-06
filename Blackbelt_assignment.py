#import required modules
import json
from datetime import datetime

#Define function find_even() for sorting even numbers
def find_even(numbers):
	#load data as a json
	x = json.loads(json.dumps(numbers[0]))
	
	#get data in sequence into a list
	y = x['sequence'].split(', ')
	
	#convert all elements to integet
	data = list(map(int, y))
	
	#Code to find even numbers and store in list "out"
	out = []
	for item in data:
		if (item%2==0):
			out.append(item)
	return out


if __name__ == "__main__":
	
	print("The current date and time is: "+str(datetime.now()))
	#input data
	data = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
	
	#Pass data to function find_even() and get output
	even = find_even(data)
	
	#print list of even numbers
	print("\nThe even numbers are:")
	print(even)