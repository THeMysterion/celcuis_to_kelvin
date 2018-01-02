#celcuis_to_kelvin

class TooColdException(Exception):

	def __init__(self):
		print("Temp:")


def c_to_k(temp):
	
	if temp < -273.15:
		raise TooColdException("Temp is -0")
	return temp + 273.15
		
print(c_to_k(#))
	

	
