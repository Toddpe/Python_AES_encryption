#!/usr/bin/env python
from tkinter import *
from tkinter.filedialog import askopenfilename
from cryptography.fernet import Fernet

root = Tk()
root.title('File Encryptor & Decryptor')
root.geometry('516x255')
#root.configure(background='black')

def show_help_text():
    root.geometry('750x490')


def key_creator_clicked():
    key = Fernet.generate_key()
    print(key)

    file = open('key.txt', 'wb')
    file.write(key)
    print('Key saved')
    file.close()


def file_encryptor_clicked():
    
    # Get key from file
    file = open(input_key, 'rb')
    key = file.read()
    file.close

    # Open file
    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    # Save new file
    with open ('encrypted.txt', 'wb') as f:
        f.write(encrypted)
    print(encrypted)
    
    
def file_decrypt_clicked():
    # Get key from file
    file = open(input_key2, 'rb')
    key = file.read()
    file.close

    # Open file
    with open(encrypted_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    # Save new file
    with open ('final.'+file_ending.get(), 'wb') as f:
        f.write(decrypted)

def get_input_file_clicked():
    global input_file
    input_file = askopenfilename()

def get_input_key_clicked():
    global input_key
    input_key = askopenfilename()
    
def get_encrypted_file_clicked():
    global encrypted_file
    encrypted_file = askopenfilename()

def get_input_key2_clicked():
    global input_key2
    input_key2 = askopenfilename()

# FRAMES:
mainframe = LabelFrame(root, bd=1)
#mainframe.configure(background='black')
key_creator_button = Button(mainframe, text='Create New Encryption Key', padx=50, pady=10, fg='black', bg='#AFAFAF', command=key_creator_clicked)
frame1 = LabelFrame(mainframe, text='Encrypt Files',fg='black', padx=10, pady=10, bd=1)
#frame1.configure(background='black')
frame2 = LabelFrame(mainframe, text='Decrypt Files',fg='black', padx=10, pady=10, bd=1)
#frame2.configure(background='black')
    
# ENCRYPT FILES:
get_input_file = Button(frame1, text='Select Input File', padx=10, pady=3, command=get_input_file_clicked)
get_input_key = Button(frame1, text='Select Key File', padx=10, pady=3, command=get_input_key_clicked)
# Buttons:
file_encryptor_button = Button(frame1, text='Encrypt File', padx=70.4, pady=10, fg='black', bg='#AFAFAF', command=file_encryptor_clicked)

# DECRYPT FILES:
global input_file2
global input_file3
global file_ending
get_encrypted_file = Button(frame2, text='Select Encrypted File', padx=10, pady=3, command=get_encrypted_file_clicked)
get_input_key2 = Button(frame2, text='Select Key File', padx=10, pady=3, command=get_input_key2_clicked)
text3 = Label(frame2, text='File Ending (png, jpg, txt, etc.):')
file_ending = Entry(frame2, width=17, fg='#AFAFAF', bg='#CCD1D1', borderwidth=2)
# Button:
file_decryptor_button = Button(frame2, text='Decrypt File', padx=70.3, pady=10, fg='black', bg='#AFAFAF', command=file_decrypt_clicked)
    
# HELP BUTTON
help_button = Button(root, text='How To Use This Program', padx=50, pady=10, fg='black', bg='#AFAFAF', command=show_help_text) 
    
#-----------GRID PLACEMENT-------------#
# FRAMES:
mainframe.grid(row=0, column=0, sticky=W)
key_creator_button.grid(row=0, column=0)
frame1.grid(row=1, column=0, sticky=W)
frame2.grid(row=1, column=1, sticky=W)
    
# ENCRYPT:
get_input_file.grid(row=0, column=0)
get_input_key.grid(row=1, column=0)
file_encryptor_button.grid(row=3, column=0)

# DECRYPT:
get_encrypted_file.grid(row=1, column=0)
get_input_key2.grid(row=2, column=0)
text3.grid(row=3, column=0)
file_ending.grid(row=4, column=0)
    
file_decryptor_button.grid(row=5, column=0)
    
# HELP:
help_button.grid(row=2, column=0, sticky=W)

# HELP TEXT:
# Text:
text2 = Label(root, justify=LEFT, text="""
ENCRYPTING FILES:
1. Create a new encryption key (or use a pre-existing key).
2. Copy the file path of the encryption key file into the "Key File Path:" text box.
3. Copy the file path of the media to be encrypted in the "Input File Path:" text box.
4. Press "Encrypt File Using Encryption Key"
   (This will us the key to encrypt the file and store as 'encrypted.txt' in the same directory as this program)
5. Keep the key and encrypted file seperate (if they are together it does not stop anyone from accessing the file).

DECRYPTING FILES:
1. Copy the file path of the encrypted file into the "Encrypted File Path:" text box.
2. Copy the file path of the encryption key into the "Key File Path:" text box.
2. Type the file ending into the text box (this will automatical set the file to the correct file type).
3. Press "Decrypt File Using Encryption Key" the decrypted file will appear in the same directory as this program
""")
# Placement:
text2.grid(row=3, column=0)

root.mainloop()

