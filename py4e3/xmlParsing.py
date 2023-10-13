import xml.etree.ElementTree as ET 

data = '''
		<person>
			<name>Chuck</name>
			<phone type="intl">+880 1551615724 </phone>
			<email hide="no">jahirsadikmonon@gmail.com</email>
		</person>

	   '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)

if tree.find('email').get('hide') == 'no':
	print('Email', tree.find('email').text,'\n\n\n')
else:
	print('No mail.\n\n')

input = '''
			<stuff>
				<users>
					<user x="2">
						<id>001</id>
						<name>Chuck</name>
					</user>
					<user x="7">
						<id>009</id>
						<name>Borris</name>
					</user>
					<user x="8">
						<id>024</id>
						<name>Kane</name>
					</user>
				</users>
			</stuff>
		'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
	print('Name:', item.find('name').text)
	print('ID:', item.find('id').text)
	print('Attribute:', item.get("x"))