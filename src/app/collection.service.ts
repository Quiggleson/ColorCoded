import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CollectionService {

  url = 'http://localhost:5000/api'

  async getColors(filepath: string): Promise<string[]> {
    console.log('Getting colors')
    const data = await fetch(`${this.url}/colors/${filepath}`)
    return data.json();
  }

  constructor() { }
}
