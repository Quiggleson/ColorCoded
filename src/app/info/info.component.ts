import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-info',
  standalone: true,
  imports: [CommonModule],
  template: `
    <p>
      info works!
    </p>
  `,
  styleUrls: ['./info.component.css']
})
export class InfoComponent {

}
