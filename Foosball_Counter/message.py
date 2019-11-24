from boot import topic_pub
from counter import Counter


def checkMessageToSend(client, team: Counter, forcesend: bool = False):
    if team.last_counter != team.counter or forcesend:
        if client.MQTTMode:
            print('Sending message...' + team.teamName + ":" + str(team.counter))
            client.publish(topic_pub, team.teamName + ":" + str(team.counter))
        else:
            print('Locally counting...' + team.teamName + ":" + str(team.counter))

        team.last_counter = team.counter
        team.display.tm.number(team.counter)
