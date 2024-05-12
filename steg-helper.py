"""
COSI 107a Course Project: Steganography
Team: William Messenger
This program employs steghide and stegseek to enable users to embed and extract secret data
using steganography. 
"""

import os

def main():
	print("Welcome to Steganography Central.")
	
	quit = False
	while quit == False:
	
		# print the main manu and get the user's input
		print("\nMain Menu")
		choice = input("PHOTOS:\n  Press 1 to embed\n  Press 2 to extract\nAUDIO:\n  Press 3 to embed\n  Press 4 to extract\nCRACKING:\n  Press 5 to crack a secret message\nPress q to quit\n")
		
		# process user's input
		if choice == "1":
			embed(1)
		elif choice == "2":
			extract("photo")
		elif choice == "3":
			embed(2)
		elif choice == "4":
			extract("audio")
		elif choice == "5":
			crack()
		elif choice in {'Q', 'q', 'quit'}:
			quit = True						# break loop if user chooses to quit
		else:
			print("Invalid Input")
			
	print("\nGoodbye!")

# This function embeds the secret data into the cover file
def embed(type):

	# customize based on whether the cover file is image or audio
	if type == 1:
		type = "photo (.jpg or .bmp)"
	else:
		type = "audio (.wav or .au)"

	# get filenames
	pub = input(f"What is the name of the {type} file? ")
	text = input(f"What is the name of the secret data file? ")
	
	# execute embedding command
	status = os.system(f"steghide embed -cf {pub} -ef {text}")
	if status != 0:
		return -1
	
	# prompt user whether they would like to delete secret data file
	delete = input("\nWould you like to delete the secret data file (Y/N)? ")
	if delete in {'Y', 'y', 'yes'}:
		os.system(f"rm {text}")
		print(f"{text} has been deleted")

# This function extracts the secret message from a steg file, with a valid passkey
def extract(type):

	# get the filename
	pub = input(f"\nWhat is the name of the {type} file? ")
	
	# execute the extraction command
	status = os.system(f"steghide extract -sf {pub}")
	if status != 0:
		return -1
	
	# prompt user whether they would like to read the secret data found
	read = input("\nWould you like to read the secret data file (Y/N)? ")
	if read in {'Y', 'y', 'yes'}:
		text = input("Confirm the name of the secret data file: ")
		os.system(f"less {text}")
		
# This function extracts secret data from a steg file where the passkey is unknown using StegSeek
def crack():

	# get the cover filename
	pub = input(f"\nWhat is the name of the file you'd like to crack? ")
	
	# execute StegSeek
	status = os.system(f"stegseek {pub} -xf \"secret-data.out\"")
	if status != 0:
		return -1
		
	print(f"Secret data exported to \"secret-data.out\"")
	
	# prompt user whether they would like to read the secret data found
	read = input("\nWould you like to read the secret data file (Y/N)? ")
	if read in {'Y', 'y', 'yes'}:
		os.system(f"less secret-data.out")

if __name__ == "__main__":
	main()
