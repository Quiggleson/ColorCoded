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


  collectionService = inject(CollectionService);
  file: File | undefined;
  colors: string[] | undefined;
  
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
