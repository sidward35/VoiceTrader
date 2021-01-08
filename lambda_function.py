import json
import requests

#converts numbers in word form to int
def text2int(textnum, numwords={}): 
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
    
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
        scales = ["hundred", "thousand", "million", "billion", "trillion"]
    
        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def lambda_handler(event, context):
    #interpret voice input
    symbol = event['symbol'].upper().split(' ')[-1] #get the last word from voice input, in case extra words are detected
    try:
        quantity = int(event['quantity']) #this will work if the voice input for quantity is detected in number form
    except:
        quantity = text2int(event['quantity']) #this will be used if the voice input for quantity is detected in word form
    
    #make trade
    headers = {'APCA-API-KEY-ID':'ID', 'APCA-API-SECRET-KEY':'SECRET'}
    response = requests.post('https://paper-api.alpaca.markets/v2/orders', headers=headers, json={'symbol':symbol, 'qty':quantity, 'side':event['action'], 'type':'market', 'time_in_force':'day'})
    
    #send notification about trade
    return_title = 'Alpaca '+ ('Buy' if event['action']=='buy' else 'Sell') +' Order Submitted'
    return_body = 'Order to '+event['action']+' '+str(quantity)+' shares of '+symbol+' submitted.'
    requests.post('https://maker.ifttt.com/trigger/market_closed/with/key/{KEY}', params={'value1':return_title,'value2':return_body})
    
    return {
        'statusCode': 200,
        'body': response.json()
    }
