import { Component, inject } from '@angular/core';
import { FileUploadService } from '../file-upload.service';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  file: File | undefined;
  uploadService: FileUploadService = inject(FileUploadService);

  imageForm = new FormGroup({
    image: new FormControl<File|null>(null)
  });

  onChange(event: any){
    this.file = event.target.files[0];
  }
  upload(){
    this.uploadService.upload(this.file!).then((answer) =>
      console.log(answer)
    );
  }

  constructor() {
    
  }

}
