import sys
import builtins
import compileall

# from contacts import TITLE


def app(prog_name):
	print(F'prog_name: {prog_name}')

def main():
	print("This is my file to test Python's execution methods.")
	print("The variable __name__ tells me which context this file is running in.")
	print("The value of __name__ is:", repr(__name__))

	print("Hello World!")
	print("builtin module names:", repr(sys.builtin_module_names))
	print("module sys.path:", repr(sys.path))
	print(dir(sys))

	# dir() не містить списку вбудованих функцій і змінних. 
	# вони визначені в стандартному модулі builtins:
	
	print(dir(builtins))

	# Модуль compileall може створювати файли .pyc 
	# для всіх модулів у каталозі.
	compileall.compile_dir('.', force=True)

# Коли файл .py імпортується як модуль, Python встановлює спеціальну змінну __name__ - назву модуля. Однак, якщо файл запускається як окремий сценарій, __name__ встановлюється як '__main__'. Використовуючи цей факт, ви можете визначити, що відбувається під час виконання, і відповідно змінити поведінку:

# Синтаксично ідіома if __name__ == "__main__"
if __name__ == "__main__":
	main()