import machine
import time

pin_D0 = machine.Pin(16, machine.Pin.OUT)
pin_D1 = machine.Pin(5,machine.Pin.OUT)
pin_D2 = machine.Pin(4,machine.Pin.OUT)
pin_D3 = machine.Pin(0,machine.Pin.OUT)
pin_D4 = machine.Pin(2,machine.Pin.OUT)
pin_D5 = machine.Pin(14,machine.Pin.OUT)

button = machine.Pin(12, machine.Pin.IN, )
IsButtonPressed  = False



pin_D0.off()
pin_D1.off()
pin_D2.off()
pin_D3.off()
pin_D4.off()
pin_D5.off()

sleepTime = 0.5      


def ToggleGivenPin(pin, toggleDelay):
    time.sleep(toggleDelay)
    pin.on()
    time.sleep(toggleDelay)
    pin.off()
    print(button.value())
    

   

while True:
            
            
            

            if button.value() == 1 : 
                IsButtonPressed = True
                time.sleep(0.5)
                
                while IsButtonPressed:                

                    if button.value() == 0:       
                        ToggleGivenPin(pin_D0, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                        

                    if button.value() == 0:       
                        ToggleGivenPin(pin_D1, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                        

                    if button.value() == 0:       
                        ToggleGivenPin(pin_D2, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                                

                    if button.value() == 0:       
                        ToggleGivenPin(pin_D3, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                        


                    if button.value() == 0:       
                        ToggleGivenPin(pin_D4, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                                    


                    if button.value() == 0:       
                        ToggleGivenPin(pin_D5, sleepTime)
                    else:
                        IsButtonPressed = False
                        sleepTime = 0.5
                        time.sleep(1)
                        break
                                         
                    
                                           

                    if sleepTime > 0.1 :
                        sleepTime = sleepTime - 0.1
                    else:
                        sleepTime = 0.5

                        
            
            


# Pin mappings
# D0 -> GPIO16
# D1 -> GPIO5
# D2 -> GPIO4
# D3 -> GPIO0
# D4 -> GPIO2
# D5 -> GPIO14
