file= open('youtube.txt', 'w')

# This is used for database interactions
try:
    file.write('Hello World')
finally:
    file.close()
    

# This is used for file handling
with open('youtube.txt', 'w') as file:
    file.write('Hello World')