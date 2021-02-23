from datetime import date, datetime, timedelta
import pandas as pd
import requestsfrom bs4 
import BeautifulSoup
import json
today = datetime.now().strftime(‘%Y-%m-%d’)
#today = '2019-10-29'
regionalHolidaysList = []
for result in results:    
     date = result.contents[0].text + ', ' + datetime.today().strftime('%Y')    
     weekday = result.contents[1].text    
     holidayName = result.contents[2].text    
     observance = result.contents[3].text     
     stateObserved = result.contents[4].text
     regionalHolidaysList.append((date, weekday, holidayName, observance, stateObserved))regionalHolidayDf = pd.DataFrame(regionalHolidaysList, columns = ['date', 'weekday', 'holidayName', 'observance', 'stateObserved'])regionalHolidayDf['date'] = regionalHolidayDf['date'].apply(lambda x: (datetime.strptime(x, '%b %d, %Y').strftime('%Y-%m-%d')))
     dateList = regionalHolidayDf['date'].tolist()
     https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
     #So we get the date if it is in this list it will send a message in slackif today in dateList:
     todayHoliday = regionalHolidayDf[regionalHolidayDf['date'] ==          today]    
     info=[]    
     for holiday in todayHoliday.itertuples():
          info.append(':umbrella_on_ground:' +                       holiday.holidayName +  ' in ' +                      holiday.stateObserved.replace('*', ''))    
     if len(info) >1:        
          infoFinal = '\n'.join(info)    
     else:        
       infoFinal = info[0]#Here is where we can format the slack message, it will output any holiday with todays

     message = f'@here Fun fact! \n Today({today}) is: \n {infoFinal}'        
     print('Sending message to the happyholiday channel...')
     slackmsg = {'text': message}    #Using the module json it formats it where the slack API can accept it
#we can store the slack link into a variable called webhook        webhook='https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
response = requests.post(webhook,  data=json.dumps(slackmsg), headers={'Content-Type': 'application/json'})    
     if response.status_code != 200:        
          raise ValueError('Request to slack returned an error %s, the response is:\n%s'            % (response.status_code, response.text)        )    
     print('Request completed!')
else:    
     print('No regional holiday today! See you next time!')
