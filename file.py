import fresh_tomatoes
import media

bb_ki_vines = media.Movie("bb ki vines","happy naukar episode","http://s1.dmcdn.net/Nq7Px/1280x720-zAK.jpg","https://www.youtube.com/watch?v=w0w7PrZS40w")

bb_ki_vine = media.Movie("bb ki vines","fameer fudde episode","https://i.ytimg.com/vi/j1WL3Ysi9jo/maxresdefault.jpg","https://www.youtube.com/watch?v=1RN1e49h9NE")

toy_story = media.Movie("toystory","toy story movie trailer","http://harlemtoys.com/wp-content/uploads/2016/03/toy-story-2-characters.jpg","https://www.youtube.com/watch?v=Bj4gS1JQzjk")

shivay = media.Movie("shivay", "shivay movie trailer","https://upload.wikimedia.org/wikipedia/en/a/a1/Ajay_Devgan's_Shivaay_poster.jpg","https://www.youtube.com/watch?v=poLjq0u4_5A")

movie = [bb_ki_vines, bb_ki_vine, toy_story, shivay]
fresh_tomatoes.open_movies_page(movie)
