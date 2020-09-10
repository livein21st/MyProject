import asyncio
from kasa import SmartBulb
import time

# 'async' transform our main() into an asynchronous function
async def main():
    # Call the definition of a light bulb, replace the IP address with the one found with kasa discover
    bulb = SmartBulb("192.168.1.110") #Make sure to replace your smart-bulb IP Address here

    # 'await' tells the program to wait till getting a result from the light bulb
    result = await bulb.get_light_state()
    print (result)

    #Example if condition
    if result['on_off'] == 1: #If the light bulb is ON
        print("Light was ON, I turned it OFF")
        await bulb.turn_off() #Turn_Off the bulb
    else:
        print("Light was OFF, I turned it ON")
        await bulb.turn_on() #Turn_On the bulb if it is OFF

    #Getting the current stat of light bulb after updating it previous stat above.
    result = await bulb.get_light_state()
    print (result)

    ## Example of for loop
    for x in range(10): # Here we are asking to loop the below code for 10 times
        await bulb.turn_on() #Turn on the light
        print("Loop: ",x) #print current loop number
        time.sleep(1.0) #sleep for 1 seconds
        await bulb.turn_off() #turn off the light
        print("Loop: ",x) #print current loop number
        time.sleep(1.0)#sleep for 1 seconds
        time.sleep(1.0)

    myIterator = iter(result)
    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))

    for x in result:
        print(x)

# We call main() in the asynchronous environment
asyncio.run(main())