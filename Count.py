class Count:
	title = ""
	element = []

	def __init__( self, s ):
		self.title = s		
	
	def addElement( self, s ):
		self.element.append(s)


c = Count( "Battery" )

print c.title
c.addElement("Intent")
c.addElement("Contact")
c.addElement("Harm")
print c.element
