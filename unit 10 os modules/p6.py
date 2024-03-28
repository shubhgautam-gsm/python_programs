import os

try:
    # If file does not exist, then it throws an IOError
    filename = 'pr1.py'
    with open(filename, 'r') as f:
        text = f.read()
        print(text)
    # The control jumps directly to here if any line throws an IOError.
except IOError:
    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)
