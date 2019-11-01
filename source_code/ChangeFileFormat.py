#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'circlezhou'

import os
from os import listdir
from os.path import isfile, join

def change_file_format(path):
	onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
	# print(onlyfiles)
	for file in onlyfiles:
		count = 0
		with open(os.path.join(path, file), 'r') as handle:
			print('modifying {}'.format(handle.name))
			lines = handle.readlines()
			lines[0] = '#!/usr/bin/env python\n'
			lines[1] = '# -*- coding: utf-8 -*-\n'
		with open(os.path.join(path, file), 'w') as handle:
			handle.writelines(lines)


if __name__ == '__main__':
	path = os.path.dirname(os.path.abspath(__file__))
	change_file_format(path)

