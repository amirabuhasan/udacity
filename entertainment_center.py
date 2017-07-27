import media
import fresh_tomatoes

boyhood = media.Movie("Boyhood",
                        "depicts the childhood and adolescence of Mason Evans Jr. from ages six to eighteen as he grows up in Texas with divorced parents" ,
                        "https://upload.wikimedia.org/wikipedia/en/b/bb/Boyhood_film.jpg",
                        "https://www.youtube.com/watch?v=Ys-mbHXyWX4")

#print (toy_story.storyline)


guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                    "In Guardians of the Galaxy, Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact." ,
                    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                    "https://www.youtube.com/watch?v=d96cjJhvlMA")

#print (avatar.storyline)
#avatar.show_trailer()


birdman = media.Movie("Birdman",
                    "A story about a faded Hollywood actor best known for playing the superhero, Birdman." ,
                    "https://upload.wikimedia.org/wikipedia/en/6/63/Birdman_poster.png",
                    "https://www.youtube.com/watch?v=uJfLoE6hanc")

#birdman.show_trailer()

before_sunset = media.Movie("Before Sunset",
                    "The film picks up the story in Before Sunrise of the young American man and French woman who spent a passionate night together in Vienna." ,
                    "https://upload.wikimedia.org/wikipedia/en/d/d1/Before_Sunset_poster.jpg",
                    "https://www.youtube.com/watch?v=oI3UuneLcyU")

anywhere_but_here = media.Movie("Anywhere But Here",
                    "A mother and daughter search for success in Beverly Hills." ,
                    "https://upload.wikimedia.org/wikipedia/en/e/e8/Anywhere-but-here-movie-poster-1999-1020272455.jpg",
                    "https://www.youtube.com/watch?v=hN9MFEw9pIo")

beginners = media.Movie("Beginners",
                    "A young man is rocked by two announcements from his elderly father: that he has terminal cancer, and that he has a young male lover." ,
                    "https://upload.wikimedia.org/wikipedia/en/f/f6/Beginners_Poster.jpg",
                    "https://www.youtube.com/watch?v=rXUFUp6vsxg")

the_breakfast_club = media.Movie("The Breakfast Club",
                    "Five high school students meet in Saturday detention and discover how they have a lot more in common than they thought." ,
                    "https://upload.wikimedia.org/wikipedia/en/5/50/The_Breakfast_Club.jpg",
                    "https://www.youtube.com/watch?v=BSXBvor47Zs")

movies = [boyhood, guardians_of_the_galaxy, birdman, before_sunset, anywhere_but_here, beginners, the_breakfast_club]


fresh_tomatoes.open_movies_page(movies)
