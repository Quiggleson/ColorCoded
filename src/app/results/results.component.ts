import { Component, EventEmitter, OnInit, Output, Input, inject } from '@angular/core';
import { ResultsService } from '../results.service';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit{
  @Input() filename: any;
  @Input() unchanged_colors: any;
  @Output() step: EventEmitter<any> = new EventEmitter<any>();

  resultsService = inject(ResultsService);
  red_file: String | undefined;

  ngOnInit(): void {
    document.querySelector('#back-button')?.addEventListener('click', () => {
      this.step.emit(1)
    })

    document.querySelector('#next-button')?.addEventListener('click', () => {
      this.step.emit(0)
    })

    this.resultsService.getRed(this.filename, this.unchanged_colors).subscribe((data: any) => {
      console.log('object keys:')
      console.log(Object.keys(data))
      console.log(`${data["nored_filename"]}`)
      this.red_file = data["nored_filename"] 
    })

    console.log(`This is the results comp, unch col: ${this.unchanged_colors}`)
  }
}
