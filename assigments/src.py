''' Progarm to Reverse The sentance word'''

def string_op(string):
	str_list = string.split(' ')
	str_list.reverse()
	return str(' '.join(str_list))

