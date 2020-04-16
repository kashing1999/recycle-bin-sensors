#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER_1 = 23
GPIO_ECHO_1 = 24

GPIO_TRIGGER_2 = 7
GPIO_ECHO_2 = 8

GPIO_TRIGGER_3 = 20
GPIO_ECHO_3 = 21


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_1, GPIO.IN)

GPIO.setup(GPIO_TRIGGER_2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_2, GPIO.IN)

GPIO.setup(GPIO_TRIGGER_3, GPIO.OUT)
GPIO.setup(GPIO_ECHO_3, GPIO.IN)

def distance(TRIGGER, ECHO):
    # set Trigger to HIGH
    GPIO.output(TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    
    WaitTime = time.time()
    StartTime = time.time()
    StopTime = time.time()
    waiting = StartTime-WaitTime
    # save StartTime
    while GPIO.input(ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def passing_true(dist_old,SET):
    TRIGGER, ECHO = SET
    dist_new= distance(TRIGGER, ECHO)
    passing = False
    if (dist_new>dist_old+5 or dist_new<dist_old-5): #5cm 
        passing= True
    
    return dist_new, passing

def sensor_choice(choice):
    if choice ==1 :
        Trigger=GPIO_TRIGGER_1
        Echo=GPIO_ECHO_1
    elif choice ==2:
        Trigger=GPIO_TRIGGER_2
        Echo=GPIO_ECHO_2
    elif choice ==3:
        Trigger=GPIO_TRIGGER_3
        Echo=GPIO_ECHO_3
    else:
        print("Not valid choice")
        return False
    Set= (Trigger, Echo)
    print (choice)
    dist_old= distance(Trigger,Echo)
    countdown=time.time()
    countdown_end=time.time()
    countdown_diff=countdown_end-countdown
    while countdown_diff<15:
        passing_through = False
        dist_old, passing_through= passing_true (dist_old,Set)
        if (passing_through): #5cm
            print ("Passing through")
            passing_through= False
            return True, 'True'
        
        countdown_end=time.time()
        time.sleep(0.0005)
        countdown_diff=countdown_end-countdown
    print ('Time overlap')
    return False, 'False'
if __name__ == '__main__': #def passing_true(), return true flase value, update distance:
    try:
        while True:
            choice = input("Enter your name: ")
            if choice.isdigit():
                thrown, thrown_string= sensor_choice(int (choice))
            else:
                print('choice not valid')
            
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

 
