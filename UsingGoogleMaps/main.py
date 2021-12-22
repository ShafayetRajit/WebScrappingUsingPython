import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:]) #get address from CMD
else:
    address = pyperclip.paste() #get address from clipboard

webbrowser.open('https://www.google.com/maps/place/'+address)


#NoteToSelf
#works well with regions ie 'Dhaka, Bangladesh' or 'LA, USA'
#doesnt work well with specefic names ie 'North South University, Bangladesh'

#important resources
#https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/


