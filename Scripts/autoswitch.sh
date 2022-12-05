#!/bin/ash
target="HUB" #eth0/USB10/LAN 
echo host > /sys/kernel/debug/usb/ci_hdrc.0/role
sleep 5
result=$(dmesg lsusb | grep "${target}")
if [[ "$result" != "" ]]
then
    echo "done"
else
    echo gadget > /sys/kernel/debug/usb/ci_hdrc.0/role
    echo "false"
fi
