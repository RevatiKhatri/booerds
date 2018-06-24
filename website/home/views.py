from django.shortcuts import render

# Create your views here.
def index(request):
	# For the homepage, context will get two things from the Database.
	# The first being the featured books. It may need to get all the books
	# then we filter them down to a certain number or we need to find a way
	# to store the certain number in the Database and just get those.
	# The second would be one or more Promotions for the header.
	context = {
		'featured_books': [
			{
				'title': "Harry Potter and the Philosopher's Stone",
				'id': '0',
				'summary': "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J. K. Rowling.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Chamber of Secrets",
				'id': '1',
				'summary': "Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/5/5c/Harry_Potter_and_the_Chamber_of_Secrets.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Prisoner of Azkaban",
				'id': '2',
				'summary': "Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author J. K. Rowling and the third in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/a/a0/Harry_Potter_and_the_Prisoner_of_Azkaban.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Goblet of Fire",
				'id': '3',
				'summary': "Harry Potter and the Goblet of Fire is a fantasy book written by British author J. K. Rowling and the fourth novel in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/c/c7/Harry_Potter_and_the_Goblet_of_Fire.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
		],
		# This may need to eventually because a dictionary object/array of
		# Promotions instead of one single promotion, if we have a slideshow
		# header on the home page.
		'promotion': {
			'sale': "50% Off All Books!",
			'detail': "Save 50% Off All Books on the ENTIRE Site!"
		},
	}
	return render(request, 'home/index.html', context)

def books(request):
	context = {
		'book_list': [
			{
				'title': "Harry Potter and the Philosopher's Stone",
				'id': '0',
				'summary': "Harry Potter and the Philosopher's Stone is a fantasy novel written by British author J. K. Rowling.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Chamber of Secrets",
				'id': '1',
				'summary': "Harry Potter and the Chamber of Secrets is a fantasy novel written by British author J. K. Rowling and the second novel in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/5/5c/Harry_Potter_and_the_Chamber_of_Secrets.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Prisoner of Azkaban",
				'id': '2',
				'summary': "Harry Potter and the Prisoner of Azkaban is a fantasy novel written by British author J. K. Rowling and the third in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/a/a0/Harry_Potter_and_the_Prisoner_of_Azkaban.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
			{
				'title': "Harry Potter and the Goblet of Fire",
				'id': '3',
				'summary': "Harry Potter and the Goblet of Fire is a fantasy book written by British author J. K. Rowling and the fourth novel in the Harry Potter series.",
				'img': {
					'url': 'https://upload.wikimedia.org/wikipedia/en/c/c7/Harry_Potter_and_the_Goblet_of_Fire.jpg',
				},
				'price': "9.99",
				'rating': '4',
			},
		],
	}
	return render(request, 'home/books.html', context)
