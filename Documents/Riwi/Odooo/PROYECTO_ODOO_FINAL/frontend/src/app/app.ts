import { Component, OnInit, signal } from '@angular/core'; // <--- Importamos signal
import { CommonModule } from '@angular/common';
import { ApiService } from './services/api.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  // CAMBIO 1: Convertimos leads en una señal vacía
  leads = signal<any[]>([]); 

  constructor(private api: ApiService) {}

  ngOnInit() {
    console.log("Pidiendo datos a Django...");
    this.api.getLeads().subscribe(
      (data) => {
        console.log('¡Datos llegaron!', data);
        // CAMBIO 2: Usamos .set() para actualizar la señal
        this.leads.set(data); 
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }
}