# -*- coding: UTF-8 -*-
import webbrowser
import os
import re
import sys


main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Movie Trailers</title>       

    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous" />
    <link rel="stylesheet" type="text/css" href="/static/css/styles.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="description">
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="description_N">
            <h2> Movie Trailers </h2>
          </div>
        </div>
      </div>
    </div>


<!-- Carousel slide BEGIN -->
<div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
    <li data-target="#myCarousel" data-slide-to="2"></li>
    <li data-target="#myCarousel" data-slide-to="3"></li>
   </ol>

<!-- Wrapper for Carousel slide -->
<div class="carousel-inner">
          {content_carousel_first_movie}
          {content_carousel}
</div>

<!-- Carousel slide Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
<!-- Carousel slide END -->


<!-- Movie trailers -->
<div class="container">
      {movie_tiles}
</div>

</div>
</body>
</html>
'''



movie_carousel_content_first = '''
    <div class="item active">
      <img src="/static/img/{carousel_image}" alt="{movie_title}" class="imagen_carousel" >
      <div class="carousel-caption">
        <h2>{movie_title}</h2>
        <div class="text_N1">
                <p>{movie_storyline}</p>
        </div>
      </div>
    </div>
'''



movie_carousel_content = '''
    <div class="item">
      <img src="/static/img/{carousel_image}" alt="{movie_title}" class="imagen_carousel" >
      <div class="carousel-caption">
        <h2>{movie_title}</h2>
        <div class="text_N1">
                <p>{movie_storyline}</p>
        </div>
      </div>
    </div>
'''



movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="300" height="390">
    <h2>{movie_title}</h2>
 </div>
'''

def create_movie_carousel_first(movie_carousel_first):
    
    content_carousel_first_movie  = ''
    for movie in movie_carousel_first:
        content_carousel_first_movie +=movie_carousel_content_first.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            carousel_image=movie.carousel_image
        )
    return content_carousel_first_movie


def create_movie_carousel(movies_carousel):
    
    content_carousel  = ''
    for movie in movies_carousel:
         content_carousel += movie_carousel_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            carousel_image=movie.carousel_image
        )
    return content_carousel



def create_movie_tiles_content(movies):
    
    content = ''
    for movie in movies:
        
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies, movie_carousel_first, movies_carousel):
    
    output_file = open('./templates/index.html', 'w')

  
    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies),
                                              content_carousel_first_movie=create_movie_carousel_first(movie_carousel_first),
                                              content_carousel=create_movie_carousel(movies_carousel))

  
    output_file.write(main_page_head + rendered_content)
    output_file.close()

   #carrega o browser auto
   # url = os.path.abspath(output_file.name)
   # webbrowser.open('file://' + url, new=2) 

