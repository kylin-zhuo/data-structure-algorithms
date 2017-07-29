import os

paths = os.listdir('.')


for f in paths:

	if os.path.isfile(os.path.join('.', f)):
		if f[:3] == 'no-':
			os.rename(os.path.join('.', f), os.path.join('.', f[3:]))

exit()

print paths

for path in paths:

	if os.path.isdir(path) and path[0] != '.':
		

		files = os.listdir(path)
		for file in files:
			
			if os.path.isfile(os.path.join(path, file)) == True:

				if file[:3] == 'no-': 
					newname = file[3:]
				elif file[:2] == 'no':
					newname = file[2:]
				else:
					newname = file

				os.rename(os.path.join(path, file), os.path.join(path, newname))


