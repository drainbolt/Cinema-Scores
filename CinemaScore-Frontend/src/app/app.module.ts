import { BrowserModule } from '@angular/platform-browser';
import { NgModule, Input } from '@angular/core';
import { TitleBarComponent } from './title-bar/title-bar.component';
import { SearchBarComponent } from './search-bar/search-bar.component';
import { MovieCardComponent } from './movie-card-component/movie-card-component';
import { ModalDialogComponent } from './modal-dialog/modal-dialog-component';

import { AppComponent } from './app.component';
import { SingleMovieComponent } from './single-movie-component/single-movie-component';
import { HttpClientModule } from '@angular/common/http';

import { InfiniteScrollModule } from 'ngx-infinite-scroll';


@NgModule({
  declarations: [
    AppComponent,
    TitleBarComponent,
    SearchBarComponent,
    MovieCardComponent,
    SingleMovieComponent,
    ModalDialogComponent,
  ],
  imports: [
    BrowserModule, HttpClientModule, InfiniteScrollModule,
  ],
  // exports: [InfiniteScrollModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
