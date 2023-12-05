import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResultsService {

  constructor(private http: HttpClient) {}

  url = 'http://localhost:5000/api'

  getRed(filename: string, unchanged_colors: number[]): Observable<Object> {
    return this.http.post(`${this.url}/red/${filename}`, {"colors": unchanged_colors});
  }
}
