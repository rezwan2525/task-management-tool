import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { config } from '../config';

@Injectable({
  providedIn: 'root'
})
export class AppHttpService {


  constructor(
    private http: HttpClient,
  ) { }

  get(url: string, params?: any ) {
    return this.http.request('GET', config.api.baseUrl + url, {
      params: new HttpParams({ fromObject: params }),
      headers: new HttpHeaders({
        Authorization: 'Token 6d1837911dbfb85218ed15dbf1319a2bebe86066',
      }),
    });
  }

  post(url: string, body: any,  params: any = {}): Observable<any> {
    return this.http.request('POST', config.api.baseUrl + url, {
      body: body,
      params: new HttpParams({ fromObject: params }),
      headers: new HttpHeaders({
        "Content-Type": "application/json",
        "Authorization": "Token 6d1837911dbfb85218ed15dbf1319a2bebe86066",
      }),
    });
  }


}
