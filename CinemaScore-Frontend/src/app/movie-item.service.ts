import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import * as uuidv4 from 'uuid/v4';
import * as $ from 'jquery';


@Injectable({
    providedIn: 'root'
})

export class MovieItemService {
    movies = [];
    movies2 = [];
    pageNum = 1;
    id = 0;
    readonly URL = 'http://localhost:5000';
    temp;

    constructor (private http: HttpClient) {}


    addMovie (movieItem) {
        movieItem.id = uuidv4();
        console.log(movieItem.id);
        this.movies.push (movieItem);
        this.movies2.push (movieItem);
    }

    add (name, language, image, imdb, rt, meta) {
        this.movies.push ({
            id: this.id,
            title: name,
            language: language,
            imageURL: image,
            IMDB: imdb,
            rottenTomatoes: rt,
            metacritic: meta,
            display: true,
        });
        this.movies2.push ({
            id: this.id,
            title: name,
            language: language,
            imageURL: image,
            IMDB: imdb,
            rottenTomatoes: rt,
            metacritic: meta,
            display: true,
        });
        this.id++;
    }

    delete (movieItem) {
        const index = this.movies.indexOf(movieItem);
        if (index >= 0) {
            this.movies.splice (index, 1);
        }
    }

    get() {
        return this.movies;
    }

    extractValues (value, obj) {
        console.log(value);
        Object.keys(value).forEach(function (key) {
            if (value[key]["imdb"] == null) {
                value[key]["imdb"] = '?'
            }
            if (value[key]["rotten_tomatoes"] == null) {
                value[key]["rotten_tomatoes"] = '?'
            }
            if (value[key]["metacritic"] == null) {
                value[key]["metacritic"] = '?'
            }

            let genres = value[key]["genres"][0];
            for (let i=1; i < value[key]["genres"].length; i++) {
                if (i==2) {
                    break;
                }
                genres += ", ";
                genres += value[key]["genres"][i]
            }
            obj.add(key, genres, value[key]["cover url"], value[key]["imdb"], value[key]["rotten_tomatoes"], value[key]["metacritic"]);
        });
    }

    pullMovies() {
        const headers = new HttpHeaders();
        // headers.set("Host", "localhost:5000");
        // headers.set("User-Agent", "PostmanRuntime/7.20.1");
        // headers.set("Accept", "*/*");
        // headers.set("Cache-Control", "no-cache");
        // headers.set("Postman-Token", "41d37c0a-5138-4ae6-bb34-23c832a33890,a60958b5-c7ec-4e05-859b-6e88e405823f");
        // headers.set("Host", "localhost:5000");
        // headers.set("Accept-Encoding", "gzip, deflate");
        // headers.set("Connection", "keep-alive");
        // headers.set("cache-control", "no-cache");

        this.http.get(this.URL + '/movieinfo/' + this.pageNum, { headers })
            .subscribe(value => this.extractValues(value, this));
        this.pageNum++;
    }

    showModal(value, obj) {
        console.log("showModal")
        let ele = document.getElementById('modalTemp');

        if (value["imdb"] == null) {
            value["imdb"] = '?'
        }
        if (value["rotten_tomatoes"] == null) {
            value["rotten_tomatoes"] = '?'
        }
        if (value["metacritic"] == null) {
            value["metacritic"] = '?'
        }

        document.getElementById('LabelTemp').innerHTML = obj;
        document.getElementById('temp-imdb').innerHTML = value["imdb"]
        document.getElementById('temp-rt').innerHTML = value["rotten_tomatoes"]
        document.getElementById('temp-meta').innerHTML = value["metacritic"]

        // let but = document.createElement("BUTTON");
        // but.setAttribute("data-toggle", "modal");
        // but.setAttribute("data-target", "modalTemp");
        // // document.appendChild(but);
        // but.click();

        document.getElementById('tempModalBut').click();
    }

    filter(str) {
        this.http.get(this.URL + '/'+str)
            .subscribe (value => this.showModal (value, str));
    }


}