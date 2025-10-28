#!/usr/bin/env python3
from inputs.inputSC import inputSuperclass

#intIO is internal IO

#we like to pretend this is input around these parts
#we nolonger doh tis

from time import sleep
# pip install sdbus
import sdbus
#i do not know why this is here
#i now know why this is here
#fuck you
#fuck you


#from sdbus import the simple dbus interface
from sdbus import DbusInterfaceCommon, dbus_method, dbus_property, DbusObjectManagerInterface
#these are the imports for each decorator



#we instanciate a class, and we call decorator functions with our contemporary variables

#so we can call these functions without defining 

#being able to define locality on a different layer of abstraction






class manager(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1'):

    @dbus_method()  # ScanDevices() takes no arguments, returns nothing
    def ScanDevices(self) -> None:
        raise NotImplementedError









#subclass to represent a port into the dbus
class modem(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem'):
    
    @dbus_method('b')  # input: boolean
    def Enable(self, enable: bool) -> None:
        raise NotImplementedError


    @dbus_property('(ub)', property_name='SignalQuality')
    def signal_quality(self) -> tuple:
        """Get signal quality as (quality_percentage, recent_flag)"""
        raise NotImplementedError











class messaging(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Messaging'):

    @dbus_method('', 'ao')
    def List(self) -> list:
        """List all SMS message object paths."""
        raise NotImplementedError

    @dbus_method('a{sv}', 'o')
    def Create(self, properties: dict) -> str:
        """Create a new SMS message with the given properties."""
        raise NotImplementedError


    @dbus_method('o', '')
    def Delete(self, path: str) -> None:
        """Delete an existing SMS message by its object path."""
        raise NotImplementedError












# org.freedesktop.ModemManager1.Sms interface (used for sending)
class sms(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Sms'):
#call in per message

    @dbus_method()
    def Send(self) -> None:
        """Send the SMS message previously created via Messaging.Create()."""
        raise NotImplementedError



    @dbus_property('s', property_name='Text')
    def text(self) -> str:
        """Get the message text content."""
        raise NotImplementedError
    
    @dbus_property('s', property_name='Number') 
    def number(self) -> str:
        """Get the sender/recipient phone number."""
        raise NotImplementedError


    @dbus_property('u', property_name='State')
    def state(self) -> int:
        """Get the SMS state (sent/received/etc)."""
        raise NotImplementedError
    #stop you're in violation of the law (enemy of the state)


    @dbus_property('u', property_name='PduType')
    def pdu_type(self) -> int:
        """Get the SMS PDU type (deliver/submit)."""
        raise NotImplementedError




class currentModemCtrl(inputSuperclass):



    def makeSend(self, number, messageString):

        smsObjectPath = self.messagingPort.Create({'number': number,'text': messageString})

                    #maybe I should make this service name thing a varialbe.... some day.... some day...
        smsObject = sms(service_name='org.freedesktop.ModemManager1', object_path=smsObjectPath)
            #fuck you
        
        smsObject.Send()

        #creates and sends message
        None


    def getMessage(self,index):
        #gets message by mm index
        return sms(service_name='org.freedesktop.ModemManager1', object_path=self.messages[index])



    def report(self):
         #return nothing
         #or return [header, body]

        #print('reporting')

        #oldMessages = self.messages

        

        #to do with the topic of message updates:
        if len(self.messages) == 0:
            print('no Messages')
            self.messages = self.messagingPort.List()
            #the above must be found once every direction of this loop

        else:

            #here is where i figured out modem manager stores messgaes in reverse order
            #print (self.messages[0])
            #cause i did not read the documentation

            #holy how does this still point to self.messages
            oldHighInd = int(self.messages[0].split('/')[-1])

            #new messages:
            self.messages = self.messagingPort.List()

            newHighInd = int(self.messages[0].split('/')[-1])


                #look here at the index not the len cause we can delete messages in the middle
            if newHighInd > oldHighInd:

                                #bonefied sms object yo #fuck you
                currMessage = sms(service_name='org.freedesktop.ModemManager1', object_path=self.messages[0])

                #print(currMessage.text)
                #print('hiiii')

                #stuff from message object function get it

                print(currMessage.number)
                #holy runtime
                print(currMessage.text)

                return[currMessage.number, currMessage.text]






        #return None





#modem_path = '/org/freedesktop/ModemManager1/Modems/0'

    
    def __init__(self):

        self.messages = []


        self.modemDbusPath = None


        # Use the **system** bus (ModemManager lives here)
        sdbus.set_default_bus(sdbus.sd_bus_open_system())


        #instance of our little defined port to the dbus object manager
        #self.om = ObjectManager(service_name='org.freedesktop.ModemManager1', object_path='/org/freedesktop/ModemManager1')


        # Use the built-in ObjectManager interface
        self.objectManagerPort = DbusObjectManagerInterface(service_name='org.freedesktop.ModemManager1', object_path='/org/freedesktop/ModemManager1')

        #we only need to wrangle the modem path out of the mouth of satan once bc we only have one modem, everhything ehich does nto ecplciiylu need ity doesnt need it and even if it did we have it now
        self.modemPort = None
        #fuck you
        #modem object

        self.getModem()

        self.modemPort.Enable(True)


        self.messagingPort = messaging(service_name='org.freedesktop.ModemManager1', object_path=self.modemDbusPath)

        #selected Message
        self.smsPort = None
        #create sms object per message

        #maybe load structure of sms objects to indexes but im lazy
        #eh its mostly already done by mm and dbus



    def getModem(self):

        objects = None

        while(not(self.modemDbusPath)):

            objects = self.objectManagerPort.get_managed_objects()

            print('lookin for Modem')

            if any('org.freedesktop.ModemManager1.Modem' in ifaces for path, ifaces in objects.items()) :
                
                self.modemDbusPath = next(path for path, ifaces in objects.items() if 'org.freedesktop.ModemManager1.Modem' in ifaces)


            sleep(1)

        print('foundModem')


        #we only need to wrangle the modem path out of the mouth of satan once bc we only have one modem, everhything ehich does nto ecplciiylu need ity doesnt need it and even if it did we have it now
        self.modemPort = modem(service_name='org.freedesktop.ModemManager1', object_path=self.modemDbusPath)














#tedsting grounds
#any furhter and ill shoot

def test():

    controlModemObject = currentModemCtrl()

    print(controlModemObject.modemPort.signal_quality)





#test()