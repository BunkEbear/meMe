#!/usr/bin/env python3


# pip install sdbus
import sdbus
from sdbus import DbusInterfaceCommon, dbus_method

# Use the **system** bus (ModemManager lives here)
sdbus.set_default_bus(sdbus.sd_bus_open_system())

SERVICE = 'org.freedesktop.ModemManager1'
ROOT = '/org/freedesktop/ModemManager1'

# --- tiny interface stubs we’ll call over D-Bus ---

class ObjectManager(DbusInterfaceCommon,
                    interface_name='org.freedesktop.DBus.ObjectManager'):
    @dbus_method(result_signature='a{oa{sa{sv}}}')
    def GetManagedObjects(self):  # returns {object_path: {iface: {prop: value}}}
        raise NotImplementedError

class Modem(DbusInterfaceCommon,
            interface_name='org.freedesktop.ModemManager1.Modem'):
    @dbus_method('b')  # input: boolean
    def Enable(self, enable: bool) -> None:
        raise NotImplementedError

# (optional) USSD example:
class Ussd(DbusInterfaceCommon,
           interface_name='org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd'):
    @dbus_method('s', 's')  # input: string, output: string
    def Initiate(self, command: str) -> str:
        raise NotImplementedError

# --- use it ---

om = ObjectManager(service_name=SERVICE, object_path=ROOT)
objs = om.GetManagedObjects()

# grab the first modem object path
modem_path = next(path for path, ifaces in objs.items()
                  if 'org.freedesktop.ModemManager1.Modem' in ifaces)

# enable the modem
m = Modem(service_name=SERVICE, object_path=modem_path)
m.Enable(True)

# (optional) send a USSD code and print the network’s reply
ussd = Ussd(service_name=SERVICE, object_path=modem_path)
print(ussd.Initiate('*#06#'))
