texts="mbuso" 
contexts="mbokwana" 
result=[] 
if (len(texts) < len(contexts)): 
	for l in texts: 
		if(l in contexts): 
			result.append(l) 
else: 
	for l in contexts: 
		if(l in texts): 
			result.append(l) 
print("Common letters:", result)