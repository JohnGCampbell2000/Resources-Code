from collections import Counter
file = open("stride4.txt")
fileLines = [sentence.split() for sentence in file]
data = {} # key values data structure linked to process names
matrix = [] # matrix used to build as range increases
processes = []
counter = -1
for fileLine in fileLines:
    data[fileLine[0]] = (1000 / float(fileLine[1]))
for index in range(101):
  if (index == 0):
    processRow = []
    for prop in data.keys(): # setting proccessRow to zero for start
      processRow.append(0)
    matrix.append(processRow)
    start = '   '.join([str(elem) for elem in processRow])
  else:
    processRow = []
    previousProcessRow = matrix[index - 1] # getting list of last iteration
    previousProcessRowLowestValue = min(previousProcessRow) # finding lowest value from previous row
    previousProcessRowLowestValueIndex = previousProcessRow.index(previousProcessRowLowestValue) # finding index of lowest value from previous line
    previousProcessRowLowestValueProcessName = list(data)[previousProcessRowLowestValueIndex] # finding the process name of the lowest value index from previous process row
    previousProcessRowLowestValueProcessValue = data[previousProcessRowLowestValueProcessName] # getting the value from the key based on process name it's tied to
    for i in range(len(data.keys())): #iterating over the data keys list
      if (i == previousProcessRowLowestValueIndex): # seeing if i is the same index of previous lowest value
        processRow.append((previousProcessRowLowestValue + previousProcessRowLowestValueProcessValue)) # if it is, we add onto the process value
        processes.append(previousProcessRowLowestValueProcessName)
      else:
        processRow.append(previousProcessRow[i]) # otherwise add onto previous lowest values index
    matrix.append(processRow)
print('  '.join(list(data)))
for processRow in matrix:
  if(counter != 99):
    displayProcesess = processes
    counter += 1
    final = [round(num, 1) for num in processRow]
    strings = '{} {} runs next'.format(final, displayProcesess[counter])
    print(strings)
  else:
    break

perecentages = Counter(displayProcesess)
s = sum(perecentages.values())
for i, a in perecentages.items():
    pct = a * 100 / s
    print(i, pct, '%')
