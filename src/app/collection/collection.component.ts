import { Component, EventEmitter, Input, OnInit, Output, inject } from '@angular/core';
import { CollectionService } from '../collection.service';

@Component({
  selector: 'app-collection',
  templateUrl: './collection.component.html',
  styleUrls: ['./collection.component.css']
})

export class CollectionComponent implements OnInit{
  @Input() filename: any;
  @Output() step: EventEmitter<any> = new EventEmitter<any>();
  @Output() unchanged_colors: EventEmitter<any> = new EventEmitter<any>();


  collectionService = inject(CollectionService);
  file: File | undefined;
  colors: string[] | undefined;
  
  addUnchangedColors(unchanged_colors_text: string): void {
    console.log('adding unchanged colors')
    console.log(unchanged_colors_text)
    unchanged_colors_text = unchanged_colors_text
      .replaceAll('[', '')
      .replaceAll(']', '')
      .replaceAll('(', '')
      .replaceAll(')', '')
      .replaceAll(' ', '')
    const split_newline = unchanged_colors_text.split("\n");
    var unchanged_colors: number[][] = [];
    split_newline.forEach((line) => {
      var rgb_text = line.split(',')
      console.log(`rgb text: ${rgb_text}`)
      const rgb: number[] = [];
      rgb_text.forEach((num) => {
        rgb.push(parseInt(num))
      })
      unchanged_colors.push(rgb)
    });
    console.log(unchanged_colors)
    this.unchanged_colors.emit(unchanged_colors)
  }

  appendColorToTextarea(color: string){
    var rgb: number[] = []
    rgb.push(parseInt(color.substring(2,4), 16))
    rgb.push(parseInt(color.substring(4,6), 16))    
    rgb.push(parseInt(color.substring(6,8), 16))
    const textarea = document.querySelector('#colors_text') as HTMLTextAreaElement;
    if(textarea.value.length === 0){
      textarea.value += `[${rgb}]`;  
    } else {
      console.log(`text area length: ${textarea.value.length}`)
      textarea.value += `\n[${rgb}]`;
    }
  }
  
  constructor() {
  }

  ngOnInit(): void {
    
    document.querySelector('#back-button')?.addEventListener('click', () => {
      this.step.emit(0)
    })

    document.querySelector('#next-button')?.addEventListener('click', () => {
      this.step.emit(2)
    })

    this.collectionService.getColors(this.filename).then(data => {
      this.colors = data;
    })
  }

}
