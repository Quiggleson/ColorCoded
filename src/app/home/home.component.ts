import { Component, inject } from '@angular/core';
import { FileUploadService } from '../file-upload.service';
import { CollectionService } from '../collection.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent {
  
  uploadService: FileUploadService = inject(FileUploadService);
  collectionService: CollectionService = inject(CollectionService);
  
  step: number = 0;
  filepath: any;

  onImageUploaded(filepath: any) {
    console.log(filepath)
    this.filepath = 'http://localhost:5000/' + filepath;
    this.step = 1;
  }
  constructor() {}
}