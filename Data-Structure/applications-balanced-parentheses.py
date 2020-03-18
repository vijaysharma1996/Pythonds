##check balanced parentheses
from pythonds.basic import Stack

def parChecker(strings):
    s=Stack()
		balanced=True
		i=0
		while i <=len(strings)) and balanced:
		    symbol=strings[i]
				if symbol="([{":
				    s.push(symbol)
				else:
				    if s.isEmpty():
						    balanced=False
						else:
				        top=s.pop()
								if not matches(top,symbol):
								       balanced= False
			   i+=1
		 if balanced and s.isEmpty():
		    return True
		 else:
		    return False
				
def matches(open,close):
    opens="([{"
		closes=")]}"
		return opens.index(open)==closes.index(close)
		   
