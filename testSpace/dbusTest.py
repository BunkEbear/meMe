#!/usr/bin/env python3


# pip install sdbus
import sdbus




#from sdbus import the simple dbus interface
from sdbus import DbusInterfaceCommon, dbus_method




# Use the **system** bus (ModemManager lives here)
sdbus.set_default_bus(sdbus.sd_bus_open_system())

SERVICE = 'org.freedesktop.ModemManager1'
#ROOT = '/org/freedesktop/ModemManager1'

# --- tiny interface stubs we’ll call over D-Bus ---



#object manager 
class ObjectManager(DbusInterfaceCommon, interface_name='org.freedesktop.DBus.ObjectManager'):
    


                                #stuff to define how the message is shaped
    @dbus_method(result_signature='a{oa{sa{sv}}}')
    # a decorator for the upcoming function

    def GetManagedObjects(self):  # returns {object_path: {iface: {prop: value}}}
        raise NotImplementedError
        #we do this 



#we instanciate a class, and we call decorator functions with our contemporary variables

#so we can call these functions without defining 

#being able to define locality on a different layer of abstraction







class Modem(DbusInterfaceCommon, interface_name='org.freedesktop.ModemManager1.Modem'):
    



    @dbus_method('b')  # input: boolean
    def Enable(self, enable: bool) -> None:
        raise NotImplementedError










# (optional) USSD example:
#class Ussd(DbusInterfaceCommon,
#           interface_name='org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd'):
##    
#    
#    @dbus_method('s', 's')  # input: string, output: string
#    def Initiate(self, command: str) -> str:
#        raise NotImplementedError




# --- use it ---




#om = ObjectManager(service_name=SERVICE, object_path=ROOT)











#objs = om.GetManagedObjects()
#i guess it returns an itterator 




# grab the first modem object path


#modem_path = next(path for path, ifaces in objs.items()
#                  if 'org.freedesktop.ModemManager1.Modem' in ifaces)

#ohhhhhh this is unneccesary we only have 1 modem and its modem0



modem_path = '/org/freedesktop/ModemManager1/Modems/0'




# enable the modem
m = Modem(service_name=SERVICE, object_path=modem_path)
m.Enable(True)


#also somewhat unneccesaty bc i already enable through mmcli in martyr




# (optional) send a USSD code and print the network’s reply
#ussd = Ussd(service_name=SERVICE, object_path=modem_path)
#print(ussd.Initiate('*#06#'))
