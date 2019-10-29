import { Component, OnInit, OnDestroy } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { IMqttMessage, MqttService } from 'ngx-mqtt';
import { S_IFMT } from 'constants';
import { MQTT_CONNECTED_MESSAGE, MQTT_PUBLISH_TOPIC } from '../app.module';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, OnDestroy {

  private subscription: Subscription;
  public message: string[];
  public team1: string;
  public team2: string;

  constructor(private mqttService: MqttService) {
    this.team1 = '0';
    this.team2 = '0';
    this.subscription = this.mqttService.observe('counter').subscribe((message: IMqttMessage) => {
      this.message = message.payload.toString().split(':');
      if (this.message[0] === 'Team 1') {
        this.team1 = this.message[1];
      } else if (this.message[0] === 'Team 2') {
        this.team2 = this.message[1];
      }

    });
  }

  public unsafePublish(topic: string, message: string): void {
    this.mqttService.unsafePublish(topic, message, { qos: 1, retain: true });
  }
  ngOnInit(): void {
    this.unsafePublish(MQTT_PUBLISH_TOPIC, MQTT_CONNECTED_MESSAGE.concat(':', this.mqttService.clientId));
  }

  public ngOnDestroy() {
    this.subscription.unsubscribe();
  }

}
