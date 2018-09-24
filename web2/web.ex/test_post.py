import mlab
from post import Post

#1. Connect
mlab.connect()

#2. Create data
p = Post(title="C4E21", author="Nam",content="Sap den project", likes=15)
print(p.title)
print(p.author)
print(p.content)
print(p.likes)

#3. Write data
p.save()