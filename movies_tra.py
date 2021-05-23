# -*- coding: UTF-8 -*-
import fresh_tomatoes
import media


hidden_figures = media.Movie("Hidden Figures", "Hidden Figures tells the incredible untold story of Katherine Jonson (Taraji P. Henson),"\
                           "Dorothy Vaughan (Octavia Spencer) and Mary Jackson (Janelle Monae)"\
                           "brilliant African-American women working at NASA who served as the brains behind the launch into orbit of astronaut John Glenn,"\
                           "a stunning achievement that turned around the Space Race."\
                           "The visionary trio crossed all gender and racial line and inspired generations.",
                           "https://upload.wikimedia.org/wikipedia/pt/thumb/4/4b/Hidden_Figures.jpg/200px-Hidden_Figures.jpg",
                           "https://www.youtube.com/watch?v=RK8xHq6dfAo&index=11&list=PLfPBohF1uFwonlyWO2aqQyROXj0EJ1qMN", "hidden_figures.jpg")

wonder_woman = media.Movie("Wonder Woman", "Before she was Wonder Woman, she was Diana, princess of the Amazons,"\
                           "trained to be an unconquerable warrior."\
                           "Raised on a sheltered island paradise, when an American pilot crashes on their shores and tells of a"\
                           "massive conflict raging in the outside world, Diana leaves her home, convinced she can stop the threat."\
                           "Fighting alongside man in a war to end all wars, Diana will discover her full powers.. and her true destiny.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=Yrdih26Dv_g", "wonder_woman.jpg" )

avengers = media.Movie("Avengers", "Avengers: Infinity War",
                                 "https://upload.wikimedia.org/wikipedia/pt/9/90/Avengers_Infinity_War.jpg",
                                 "https://www.youtube.com/watch?v=6ZfuNTqbHE8", "Blade_runner.jpg")

jurassic = media.Movie("Jurassic World", "American science fiction adventure film",
                                          "https://upload.wikimedia.org/wikipedia/en/c/c6/Jurassic_World_Fallen_Kingdom.png",
                                          "https://www.youtube.com/watch?v=1FJD7jZqZEk", "Blade_runner.jpg")

guardians  = media.Movie("Guardians of Galaxy", "New Guardians of the Galaxy Vol2",
                                      "https://upload.wikimedia.org/wikipedia/pt/0/07/Guardians_of_the_galaxy_vol_two_poster.jpg",
                                      "https://www.youtube.com/watch?v=duGqrYw4usE", "Blade_runner.jpg")

star_wars = media.Movie("Star Wars",  "The last Jedi",
                                      "https://upload.wikimedia.org/wikipedia/pt/0/0e/Star_Wars_The_Last_Jedi.png",
                                      "https://www.youtube.com/watch?v=Q0CbN8sfihY", "Blade_runner.jpg")

jumanji = media.Movie("Jumanji", "In the brand new adventure Jumanji, Welcome to the Jungle, the tables are turned as four teenagers in detention"\
                  "are sucked into the world of Jumanji."\
                  "When they discover an old video game console with a game they have never heard of, they are immediately thrust into the game's jungle setting,"\
                  "into the bodies of their avatars, played by Dwayne Johnson, Jack Black, Kevin Hart, and Karen Gillan."\
                  "What they discover is that you don't just play Jumanji , Jumanji plays you."\
                  "They'll have to go on the most dangerous adventure of their lives, or they'll be stuck in the game forever.",
                  "https://i.ytimg.com/vi_webp/rbUb2paXWdc/movieposter.webp", "https://www.youtube.com/watch?v=2QKg5SZ_35I", "Jumanji.jpg" )

blade_runner = media.Movie("Blade Runner 2049", "Blade Runner  Thirty years after the events of the first film, a new blade runner, LAPD Officer K (Ryan Gosling),"\
                        "unearths a long-buried secret that has the potential to plunge what's left of society into chaos."\
                        "K's discovery leads him on a quest to find Rick Deckard (Harrison Ford), a former LAPD blade runner who has been missing for 30 years.",
                        "https://i.ytimg.com/vi_webp/qbRN3ZD8gI4/movieposter.webp", "https://www.youtube.com/watch?v=86XtZMgFziI" , "Blade_runner.jpg")

fast_furious = media.Movie("Fast & Furious 8", "Fast & Furious", "https://i.ytimg.com/vi_webp/Yl8zGoIW-Vo/movieposter.webp",
                                       "https://www.youtube.com/watch?v=uisBaTkQAEs", "Blade_runner.jpg")


movies = [ hidden_figures, wonder_woman, avengers, jurassic, guardians, star_wars, jumanji, blade_runner, fast_furious]
movie_carousel_first = [jumanji]
movies_carousel = [blade_runner, hidden_figures, wonder_woman]
fresh_tomatoes.open_movies_page(movies, movie_carousel_first, movies_carousel)





           
