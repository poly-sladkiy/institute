from covid import Covid
import time

def print_covid(info, i):
	print('#', i)
	print('Russia\nconfirmed:\t', info['confirmed'])
	print('active:\t\t', info['active'])
	print('deaths:\t\t', info['deaths'])
	print('recovered:\t', info['recovered'])
	print()

covid = Covid()

i = 1
russia_cases = covid.get_status_by_country_name("russia")
print_covid(russia_cases, i)

while True:
	russia_new_cases = covid.get_status_by_country_name("russia")
	if russia_new_cases['last_update'] > russia_cases['last_update']:
		i += 1
		print_covid(russia_new_cases, i)
		russia_cases = russia_new_cases

	time.sleep(1)
	pass