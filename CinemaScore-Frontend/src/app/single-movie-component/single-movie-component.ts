import { Component, Input } from "@angular/core";

@Component ({
    selector: 'single-movie-component',
    templateUrl: './single-movie-component.html',
    styleUrls: ['./single-movie-component.css']
})

export class SingleMovieComponent {
    @Input() movie;
}
