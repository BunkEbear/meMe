#!/usr/bin/env python3

from time import sleep
# pip install sdbus
import sdbus
#i do not know why this is here


#from sdbus import the simple dbus interface
from sdbus import DbusInterfaceCommon, dbus_method, dbus_property, DbusObjectManagerInterface
#these are the imports for each decorator



#we instanciate a class, and we call decorator functions with our contemporary variables

#so we can call these functions without defining 

#being able to define locality on a different layer of abstraction


#object manager 
#class ObjectManager(DbusInterfaceCommon, interface_name='org.freedesktop.DBus.ObjectManager'):
##    
#

#                                #stuff to define how the message is shaped
#    @dbus_method(result_signature='a{oa{sa{sv}}}')
#    # a decorator for the upcoming function
#
#    def GetManagedObjects(self):  # returns {object_path: {iface: {prop: value}}}
#        raise NotImplementedError
#        #we do this 







class Manager(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1'):

    @dbus_method()  # ScanDevices() takes no arguments, returns nothing
    def ScanDevices(self) -> None:
        raise NotImplementedError








#subclass to represent a port into the dbus
class Modem(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem'):
    
    @dbus_method('b')  # input: boolean
    def Enable(self, enable: bool) -> None:
        raise NotImplementedError


    @dbus_property('(ub)', property_name='SignalQuality')
    def signal_quality(self) -> tuple:
        """Get signal quality as (quality_percentage, recent_flag)"""
        raise NotImplementedError







class Messaging(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem.Messaging'):

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
class Sms(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Sms'):

    @dbus_method()
    def Send(self) -> None:
        """Send the SMS message previously created via Messaging.Create()."""
        raise NotImplementedError












class currentModemCtrl:



#modem_path = '/org/freedesktop/ModemManager1/Modems/0'

    
    def __init__(self):

        # Use the **system** bus (ModemManager lives here)
        sdbus.set_default_bus(sdbus.sd_bus_open_system())


        #instance of our little defined port to the dbus object manager
        #self.om = ObjectManager(service_name='org.freedesktop.ModemManager1', object_path='/org/freedesktop/ModemManager1')


        # Use the built-in ObjectManager interface
        self.om = DbusObjectManagerInterface(
            service_name='org.freedesktop.ModemManager1',
            object_path='/org/freedesktop/ModemManager1',
        )

        #place holder for 
        self.objs = None
        #we only need to wrangle the modem path out of the mouth of satan once bc we only have one modem, everhything ehich does nto ecplciiylu need ity doesnt need it and even if it did we have it now
        self.modemPort = None
        #fuck you
        #modem object

        self.getModem()

        self.modemPort.Enable(True)





    def getModem(self):

        modem_path = None

        while(not(modem_path)):

            self.objs = self.om.get_managed_objects()

            print('lookin for Modem')

            if any('org.freedesktop.ModemManager1.Modem' in ifaces for path, ifaces in self.objs.items()) :
                
                modem_path = next(path for path, ifaces in self.objs.items() if 'org.freedesktop.ModemManager1.Modem' in ifaces)


            sleep(1)

        print('foundModem')


        #we only need to wrangle the modem path out of the mouth of satan once bc we only have one modem, everhything ehich does nto ecplciiylu need ity doesnt need it and even if it did we have it now
        self.modemPort = Modem(service_name='org.freedesktop.ModemManager1', object_path=modem_path)





def test():

    controlModemObject = currentModemCtrl()

    print(controlModemObject.modemPort.signal_quality)


test()