import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import Dropzone from 'dropzone';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
})
export class UploadComponent implements OnInit {
  onChange(event: any) {
    console.log(event);
  }

  ngOnInit(): void {
    const myDropzone = new Dropzone('#my-dropzone');
  }

  constructor() {}
}
