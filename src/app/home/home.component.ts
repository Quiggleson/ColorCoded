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
  filename: any;
  unchanged_colors: any;

  onImageUploaded(filename: any) {
    this.step = 1;
    this.filename = filename;
  }

  onStepChange(step: any) {
    this.step = step;
  }

  onInfoPress(step: any) {
    console.log('Step is 3');
    this.step = 3;
  }

  onUnchangedColors(unchanged_colors: any) {
    console.log('unchanged colors from home: ')
    console.log(unchanged_colors)
    this.unchanged_colors = unchanged_colors;
  }

  constructor() {}
}
