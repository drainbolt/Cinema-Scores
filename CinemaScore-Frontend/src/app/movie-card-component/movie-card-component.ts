import { Component, Input, OnInit } from "@angular/core";
import { SingleMovieComponent } from '../single-movie-component/single-movie-component';
import { MovieItemService } from '../movie-item.service';


@Component ({
    selector: 'movie-card-component',
    templateUrl: './movie-card-component.html',
    styleUrls: ['./movie-card-component.css']
})

export class MovieCardComponent {
    @Input() movieCards;


    constructor (private movieItemService: MovieItemService) {}

    onScroll() {
        this.movieItemService.pullMovies();
    }

}
