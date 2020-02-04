import { Component, OnInit } from '@angular/core';
import { MovieItemService } from './movie-item.service';
import $ from 'jquery';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'CinemaScore-Frontend';
  movieTitles = ["Spider-Man: Homecoming", "Spider-Man: Far from home"]
  movies = []

  movie1 =
  {
    title: "Spider-Man: Far from home",
    language: "English",
    imageURL: "../../assets/images/SpidermanFarFromHome.jpg",
    IMDB: 10,
    rottenTomatoes: 98,
    metacritic: 89,
    display: true,
  }
  movie2 =         
  {
    title: "Spider-Man: Homecoming",
    language: "English",
    imageURL: "../../assets/images/testImage.jpg",
    IMDB: 8.8,
    rottenTomatoes: 72,
    metacritic: 70,
    display: true,
  }


  constructor (private movieItemService: MovieItemService) {

  }

  ngOnInit() {
    this.movies = this.movieItemService.get();
    this.movieItemService.pullMovies();
  }

  // addTitleSuggestions(titles) {
  //   let dl = document.getElementById("movieTitles");
  //   // let sb = document.getElementById("searchBar");
  
  //   titles.forEach(title => {
  //     let option = document.createElement("option");
  
  //     option.value = title;
  //     dl.appendChild(option);
  //   });
  // }


    // addTitleSuggestions(movieTitles);
}





