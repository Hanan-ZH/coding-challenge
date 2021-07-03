"""
This is a module for fold function ( built-in reduce function in Python )
fold(function, sequence, initialvalue(optional))

"""
   
def fold(function, sequence, init=None):
    elements  = iter(sequence) # Head at firts element of sequence
    if init==None:
    	if len(sequence)==0:
    		raise TypeError('sequence is empty') 
    	else:
    	   result=next(elements) 
    else:
    	result = init
    for i in elements: # Loop starting from second element of sequence
                       # if initial value is not given
        result = function(result, i)
    return result