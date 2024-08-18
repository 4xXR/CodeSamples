from ncclient import manager
import xml.dom.minidom

router = {"host": "sandbox-iosxr-1.cisco.com", "port": "830",
          "username": "admin", "password": "C1sco12345"}

netconf_filter = """
<filter>
  <router xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-um-router-static-cfg"/>
</filter>
"""

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

        interface_netconf = m.get_config(source = 'running', filter = netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print(xmlDom.toprettyxml(indent=" "))
        print('*' * 25 + "Break" + '*' * 50)
    m.close_session()
