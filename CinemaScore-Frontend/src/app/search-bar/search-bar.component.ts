import { Component } from '@angular/core';
import { MovieItemService } from '../movie-item.service';


@Component({
  selector: 'search-bar-component',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.css']
})
export class SearchBarComponent {
  constructor (private movieItemService: MovieItemService) {}

  onChange(str) {
    this.movieItemService.filter(str);
  }

}