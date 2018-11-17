import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AlertController } from 'ionic-angular';

import { RestProvider} from '../../providers/rest/rest'
import { HomePage } from '../home/home';
import { RegistroPage } from '../registro/registro';

/**
 * Generated class for the LoginPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-login',
  templateUrl: 'login.html',
})
export class LoginPage {
  usuario:String;
  password:String;

  
  constructor(public navCtrl: NavController
    , public navParams: NavParams
    , public restProvider: RestProvider
    , public alertCtrl: AlertController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad LoginPage');
    if(localStorage.getItem('token')){
      this.navCtrl.setRoot(HomePage);
    }
  }

  initSession(){
    console.log(this.usuario);
    console.log(this.password); 

    var data = { 'username':this.usuario, 'password':this.password };
    this.restProvider.login(data).then( (result:any) => {
    console.log(result);
    window.localStorage['token'] = result.key;
    this.navCtrl.setRoot(HomePage);
    }, (err) => {
    console.log(err);
    this.showLoginAlert();
    });
  }

  showLoginAlert() {
    const alert = this.alertCtrl.create({
      title: 'Login',
      subTitle: 'Su usuario o su contraseña no son correctos, por favor intente de nuevo',
      buttons: ['OK']
    });
    alert.present();
  }

  register(){
    this.navCtrl.push(RegistroPage);
  }

}
