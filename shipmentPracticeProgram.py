# Shipment practice program

import sys

toRestartProgram = True
def dailyShipments():   # define function dailyShipments()
    shipmentsPerDay = 50   # define shipmentsPerDay
    greetingMessage = print('Welcome to Derp Logistics, how many shipments receieved for today?')
    
   
    
    while True:
        try:
            greetingMessageInput = int(input(''))
        except ValueError:
            print('Please enter a valid number.')
            continue
        else:
            break
            
    shipmentsReceived = greetingMessageInput
    itemsPerShipment = (shipmentsReceived / shipmentsPerDay)
    
    while itemsPerShipment > 0:
        if float(itemsPerShipment) < 1:
            print('\nEach shipment requires less than 1 item.')
            print('\nHave a nice day!')
            break
        elif itemsPerShipment == 1:
            print('\nEach shipment requires approximately ' + str(int(itemsPerShipment)) + ' item.')
            print('\nHave a nice day!')
            break
        elif itemsPerShipment >= 2:
            print('\nEach shipment requires approximately ' + str(int(itemsPerShipment)) + ' items.')
            print('\nHave a nice day!')
            break
        elif (itemsPerShipment <= 99 or itemsPerShipment >= 51):
            print('\nEach shipment requires approximately ' + str(int(itemsPerShipment)) + ' item.')
            print('\nHave a nice day!')
            break
        elif float(itemsPerShipment) <= 0:
            print('Please enter a valid number.')
    
    
    while True:
        
        restartMessageInput = input(str('Would you like to start again? (Y/N) '))    
        if restartMessageInput == 'Y':
            break
        elif restartMessageInput == 'N':
            print('Good-bye')
            sys.exit()
        else:
            print('Please enter a valid option.')
            continue
        

while toRestartProgram:
    dailyShipments()
