"""
COSI 107a Course Project: Steganography
Team: William Messenger
This program manipulates an image by pixels, according to amounts inputted by the user.
"""

from PIL import Image

def main():
	image_file = input("What is the name of the image file? ")
	r = int(input("How much to adjust r value? "))
	g = int(input("How much to adjust g value? "))
	b = int(input("How much to adjust b value? "))
	adjust(image_file, r, g, b)
	
	
def adjust(image_file, r_adjust, g_adjust, b_adjust):
	
	# load the image
	input_image = Image.open(image_file)
	pixel_map = input_image.load()
	
	# get the image's dimensions
	width, height = input_image.size
	
	input_image.show()		# show the image pre-manipulation
	
	# iterate over entire image
	for i in range(width):
		for j in range(height):
		
			# get pixel RGB values
			r, g, b = input_image.getpixel((i, j))
			
			#print(f"{r} {g} {b}\n{bin(r)} {bin(g)} {bin(b)}")			# seeing how binary and decimal values change
			
			# adjust pixels by inputted factors
			r += r_adjust
			g += g_adjust
			b += b_adjust
			
			#print(f"{r} {g} {b}\n{bin(r)} {bin(g)} {bin(b)}")			# seeing how binary and decimal values change
			
			pixel_map[i, j] = (r, g, b)
			
	input_image.save("edited.jpg", format="jpeg")
		
	input_image.show()			# show the image post-manipulation
		
	
if __name__ == "__main__":
	main()
