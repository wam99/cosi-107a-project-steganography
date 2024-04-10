import os

def main():
	print("Welcome to Steganography Central.")
	
	quit = False
	while quit == False:
		print("\nMain Menu:")
		choice = input("Press 1 to embed\nPress 2 to extract\nPress q to quit\n")
		if choice == "1":
			embed()
		elif choice == "2":
			extract()
		elif choice in {'Q', 'q', 'quit'}:
			quit = True
		else:
			print("Invalid Input")
	print("\nGoodbye!")
	
def embed():
	
	status = -1
	while status != 0:
		pic = input("What is the name of the photo file? ")
		text = input("What is the name of the text file? ")
		status = os.system(f"steghide embed -cf {pic} -ef {text}")
		if status != 0:
			print("Error: Invalid Input")
	
	
	delete = input("\nWould you like to delete the text file (Y/N)? ")
	if delete in {'Y', 'y', 'yes'}:
		os.system(f"rm {text}")
		print(f"{text} has been deleted")
	
def extract():
	status = -1
	while status != 0:
		pic = input("What is the name of the photo file? ")
		status = os.system(f"steghide extract -sf {pic}")
		
	read = input("\nWould you like to read the text file (Y/N)? ")
	if read in {'Y', 'y', 'yes'}:
		text = input("What is the name of the text file? ")
		os.system(f"less {text}")

if __name__ == "__main__":
	main()
