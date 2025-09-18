def addition(a:float, b:float) -> float:
	return a + b

def subtraction(a:float, b:float) -> float:
	return a - b

def multiplication(a:float, b:float) -> float:
	return a * b

def division(a:float, b:float) -> float | str:
	if b != 0:
		return a / b
	else:
		return "Division by zero error"