import pandas as pd

def slice_func(signal,price,identify,tp_rate,sl_rate):
	"""
	:param signal: panda series
	:param price: panda series
	:param identify: int, 1 or -1
	:return: sig_slice: list, which is the new slice and value set for signal
	"""
	sig_list = signal.tolist()
	price_list = price.tolist()
	indices = [i for i, x in enumerate(sig_list) if x == identify and sig_list[i - 1] != identify]
	sig_slice = [sig_list[indices[i]:indices[i + 1]] for i in range(len(indices) - 1)]
	price_slice = [price_list[indices[i]:indices[i + 1]] for i in range(len(indices) - 1)]
	if len(indices) == 0:
		return print('No valid signal')
	if indices[0] != 0:
		sig_slice = [sig_list[0:indices[0]]] + sig_slice
		price_slice = [price_list[0:indices[0]]] + price_slice
	else:
		pass
	if indices[-1] != len(sig_list) - 1:
		sig_slice += [sig_list[indices[-1]:]]
		price_slice += [price_list[indices[-1]:]]
	else:
		sig_slice += [[sig_list[indices[-1]]]]
		price_slice += [[price_list[indices[-1]]]]
	for i in range(len(price_slice)):
		if len(price_slice[i]) == 1:
			pass
		else:
			for j in range(1, len(price_slice[i])):
				a = (price_slice[i][j] / price_slice[i][0] - 1) * identify
				# print(price_slice[i][0], price_slice[i][j], a)
				if a >= tp_rate or a <= sl_rate:
					sig_slice[i][j] = 0
				else:
					sig_slice[i][j] = ''
	return pd.Series(sum(sig_slice,[]))
