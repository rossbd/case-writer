class Element:
	elementText = ""
	factText = []

	def __init__( self, s ):
		self.elementText = s;

	def addFact( self, s ):
		self.factText.append(s)

	def assemble( self ):
		
		l = []

		for i in self.factText:
			l.append( self.elementText + " because " + i )
		
		return l				

t = Element( "Bob acted with intent" )
t.addFact("Bob announced that he was going to strike Alice.")
t.addFact("Bob faced himself in Alice's direction.")
t.addFact("Bob moved his arm of his own volition.")

print t.elementText
print t.factText

print t.assemble()
