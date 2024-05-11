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
		print("\nMain Menu")
		choice = input("PHOTOS:\n  Press 1 to embed\n  Press 2 to extract\nAUDIO:\n  Press 3 to embed\n  Press 4 to extract\nCRACKING:\n  Press 5 to crack a secret message\nPress q to quit\n")
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
			quit = True
		else:
			print("Invalid Input")
	print("\nGoodbye!")
	
def embed(type):

	if type == 1:
		type = "photo (.jpg or .bmp)"
	else:
		type = "audio (.wav or .au)"

	pub = input(f"What is the name of the {type} file? ")
	text = input(f"What is the name of the secret data file? ")
	status = os.system(f"steghide embed -cf {pub} -ef {text}")
	if status != 0:
		return -1
	
	
	delete = input("\nWould you like to delete the secret data file (Y/N)? ")
	if delete in {'Y', 'y', 'yes'}:
		os.system(f"rm {text}")
		print(f"{text} has been deleted")
	
def extract(type):

	pub = input(f"\nWhat is the name of the {type} file? ")
	status = os.system(f"steghide extract -sf {pub}")
	if status != 0:
		return -1
		
	read = input("\nWould you like to read the secret data file (Y/N)? ")
	if read in {'Y', 'y', 'yes'}:
		text = input("Confirm the name of the secret data file: ")
		os.system(f"less {text}")
		
def crack():
	pub = input(f"\nWhat is the name of the file you'd like to crack? ")
	status = os.system(f"stegseek {pub} -xf \"secret-data.out\"")
	if status != 0:
		return -1
	print(f"Secret data exported to \"secret-data.out\"")
	
	read = input("\nWould you like to read the secret data file (Y/N)? ")
	if read in {'Y', 'y', 'yes'}:
		os.system(f"less secret-data.out")

if __name__ == "__main__":
	main()
