from time import time

# Print function's answer and elapsed time taken
def print_time_and_result(function):
	def decorated(*args, **kwargs):
		start_time = time()
		result = function(*args, **kwargs)
		print("answer for {}:\t{}".format(function.__name__, result))
		print("elapsed time: {} seconds\n".format(time() - start_time))
		return result
	return decorated

def generate_rules(rules_text):
	rules = {}
	for rule in rules_text:
		key, rule_with_or = rule.split(": ")
		val1 = rule_with_or.split(" or ")[0].split("-")
		val2 = rule_with_or.split(" or ")[1].split("-")
		
		values = []
		values += [num for num in range(int(val1[0]),int(val1[1])+1)]
		values += [num for num in range(int(val2[0]),int(val2[1])+1)]
		rules[key] = values
		
	return rules


def get_good_bad_tickets_and_bad_values_and_dict_rules(my_ticket, tickets, rules_text):
	rules = generate_rules(rules_text)
	good_tickets = []
	bad_tickets = []
	bad_vals = []
	
	for ticket in tickets:
	
		for num in ticket.split(","):
		
			good_val = False
			for rule in rules:
				good_val = good_val or (int(num) in rules[rule])
			if good_val == False:
				bad_vals.append(int(num))
				bad_tickets.append(ticket)
	
	for ticket in tickets:
		if ticket not in bad_tickets:
			good_tickets.append(ticket)
				
	return sum(bad_vals), good_tickets, rules

@print_time_and_result
def part1(summed_bad_vals):
	return summed_bad_vals

@print_time_and_result
def part2(my_ticket, good_tickets, dict_rules):
	good_ticket_rows = [ticket.split(",") for ticket in good_tickets]
	good_ticket_cols = [[0 for num in range(0,len(good_ticket_rows))] for num in range(0,20)]
	
	for t_indx in range(0,len(good_ticket_rows)):
		for v_indx in range(0,20):
			good_ticket_cols[v_indx][t_indx] = int(good_ticket_rows[t_indx][v_indx])
	
	col_rules_pass = {new_list: set() for new_list in range(0,20)}
	col_counter = 0
	for col in good_ticket_cols:
		for rule in dict_rules:
			passed = True
			for value in col:
				if value not in dict_rules[rule]:
					passed = False
			
			if passed:
				col_rules_pass[col_counter].add(rule)
		
		col_counter += 1

	other = dict(sorted(col_rules_pass.items(), key=lambda item: len(item[1])))
	
	#breakpoint()
	import pdb; pdb.set_trace()
	
	return "hi"

if __name__ == '__main__':
	with open("tickets.txt","r") as file:
		tickets = file.read().splitlines()
		
	with open("mine.txt","r") as file:
		my_ticket = file.read().splitlines()
		
	with open("rules.txt","r") as file:
		rules = file.read().splitlines()

	summed_bad_vals, good_tickets, dict_rules = get_good_bad_tickets_and_bad_values_and_dict_rules(my_ticket, tickets, rules)
	
	part1(summed_bad_vals)
	part2(my_ticket, good_tickets, dict_rules)
