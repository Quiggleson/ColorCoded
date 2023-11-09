import { Component, EventEmitter, OnInit, Output } from '@angular/core';

@Component({
  selector: 'app-results',
  templateUrl: './results.component.html',
  styleUrls: ['./results.component.css']
})
export class ResultsComponent implements OnInit{
  @Output() step: EventEmitter<any> = new EventEmitter<any>();

  ngOnInit(): void {
    document.querySelector('#back-button')?.addEventListener('click', () => {
      this.step.emit(1)
    })

    document.querySelector('#next-button')?.addEventListener('click', () => {
      this.step.emit(0)
    })
  }
}
