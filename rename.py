import os

def rename():
	d = os.getcwd()
	renamed_files, exist_files = renamed_file()
	config = open('config.txt', 'a+')
	files = os.listdir(d)
	i = 0
	for f in files:
		if f in renamed_files:
			print 'The file:%s has been renamed' % f
		elif f in exist_files:
			print 'The file:%s is the renamed file'
		elif os.path.isfile(os.path.join(d, f)) and (f != 'rename.py') and \
					(f != 'config.txt'):
			while True:
				newname = str(i) + '.jpg'
				if newname in exist_files:
					i += 1
				else:
					break
			os.rename(os.path.join(d, f), os.path.join(d, newname))
			vert = str(f) + '-->' + newname + '\n'
			config.write(vert)
			i += 1
		else:
			continue
	config.close()
	print 'done'

def renamed_file():
	try:
		config = open('config.txt', 'r')
	except:
		print 'No config files'
		return [], []
	lines = config.readlines()
	config.close()
	renamed_files = []
	exist_files = []
	for vert in lines:
		file_name = vert.split('-->')
		renamed_files.append(file_name[0])
		exist_files.append(file_name[1].strip('\n'))
	return tuple(renamed_files), tuple(exist_files)
			
if __name__ == '__main__':
	rename()

