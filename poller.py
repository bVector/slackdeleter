import requests
import time

from keys import slacktoken

dayago = time.time() - 86400

getmessages = 'https://slack.com/api/channels.history?token=%s&channel=C02KTPE68&latest=%s&pretty=1' % (slacktoken, dayago)

def pollmessages():
    r = requests.get(getmessages, timeout=3.05)
    r.raise_for_status()
    for messageindex, message in enumerate(r.json()['messages']):                            
        #print messagei                                                                      
        print messageindex,                                                                  
        try:                                                                                 
            print '     deleting', message['username'], message['text'], 'at', message['ts'] 
        except KeyError:                                                                     
            print ' -   deleting',  message                                                  
        delete_message(message['ts'])                                                        
        time.sleep(0.65)

def delete_message(ts, token=slacktoken, channel='C02KTPE68'):
    ts = str(ts)
    deleteurl = 'https://slack.com/api/chat.delete?token=%s&ts=%s&channel=%s&pretty=1' % (token, ts, channel)
    r = requests.get(deleteurl, timeout=3.02)
    print r.status_code, '    ', r.json()


while True:
    pollmessages()












