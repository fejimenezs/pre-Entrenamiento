import { ApplicationConfig, provideZonelessChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideHttpClient, withFetch } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZonelessChangeDetection(), // <--- AQUÍ ESTABA EL CAMBIO (Ya es oficial)
    provideRouter(routes),
    provideHttpClient(withFetch())
  ]
};