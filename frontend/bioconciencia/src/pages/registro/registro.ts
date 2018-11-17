import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestProvider } from '../../providers/rest/rest';

/**
 * Generated class for the RegistroPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-registro',
  templateUrl: 'registro.html',
})
export class RegistroPage {

  username: String;
  password: String;

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad RegistroPage');
  }

  registro(){
/*
    var data = { 'nombre':this.nombre
    ,'apellido':this.apellido
    ,'correo':this.correo 
    ,'username':this.username
    ,'password':this.password
    ,'fecha_nacimiento':this.fecha_nacimiento
    ,'perfil':this.perfil
    };
*/
    var data = { 'username':this.username
    ,'password':this.password
    };
/*
    this.restProvider.register(data).then( (result:any) => {
      console.log(result);
      this.navCtrl.setRoot(LoginPage);
      }, (err) => {
      console.log(err);
      });    
*/
  } 

}
