import { Component, EventEmitter, OnInit, Output, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import Dropzone from 'dropzone';
import { FileUploadService } from '../file-upload.service';

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
})
export class UploadComponent implements OnInit {
  @Output() imageUploaded: EventEmitter<any> = new EventEmitter<any>();
  
  fileUploadService = inject(FileUploadService)
  sent = false;
  
  onChange(event: any) {
    console.log(event);
  }

  ngOnInit(): void {
    const myDropzone = new Dropzone('#my-dropzone',{
      url: 'http://localhost:5000/api/file-upload',
      autoProcessQueue: false,
      paramName: "image"
    });
    myDropzone.on('addedfile', (file: any) => {
      file.customData = {image: null}

      const reader = new FileReader();
      reader.onload = (event) => {
        if (event.target && event.target.result) {
          file.customData.image = event.target.result;
        }
      }
      reader.readAsDataURL(file);
      
      document.querySelector("#submit-button")?.addEventListener("click", () => {
        myDropzone.processFile(file)
      })
      
      document.querySelector("#remove-button")?.addEventListener("click", () => {
        myDropzone.removeFile(file)
      })
    })
    
    myDropzone.on('sending', (file: any, xhr: any, formData: any) => {
      const dataToSend = JSON.stringify({image: file.customData.image});
      formData.append('jsonData', dataToSend);
    })
    
    myDropzone.on('success', (file: any, response: any) => {
      this.imageUploaded.emit(response.filepath); // Emit the uploaded image data
    })
  }

  constructor() {}
}
