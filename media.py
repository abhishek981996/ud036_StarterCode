import webbrowser
'''module used for web browser based classes'''

class Movie():
	def __init__(self, movie_titles, movie_storyline, poster_image, trailer_youtube):
	
		''' __init function is a initializer and it is automatically called when instances of class movie are created
		return : this function doesnt return anything simply create space of variable for parameters
		parameters used:
		 movie_titles    = (string) initializes titles of the movie recieved from the argument passed 
		 movie_storyline = (string) initializes storyline
		 poster_image    = (string) link of the image..
		 trailer_youtube = (string) movie trailer link  '''
	
		self.title = movie_titles
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

		
	def show_trailer(self):
		''' Return : none
		parameters used : none
		simply opens the trailer link 
		'''
		webbrowser.open(self.trailer_youtube_url)
