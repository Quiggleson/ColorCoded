import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class FileUploadService {

  constructor(private http: HttpClient) { }

  async upload(file: File): Promise<Object>{
    const formData = new FormData();
    formData.append('image', file);
    return this.http.post('http://localhost:5000/api/file-upload', formData).subscribe();
  }
}
