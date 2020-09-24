filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
extension = '.hpp'
for filename in filenames:
  if filename.endswith(extension):
    newfilename = filename.replace(extension, '.h')
    newfilenames.append(newfilename)
    print(filename,newfilename)
  else:
    newfilename = filename
    newfilenames.append(newfilename)
    print(filename,newfilename)

#print (filename, newfilename) # Should be [('program.c', 'program.c'), ('stdio.hpp', 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
