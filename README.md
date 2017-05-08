# 6LowPan-Pi-Volt-Meter
From http://www.linuxjournal.com/content/low-power-wireless-6lowpan-ieee802154-and-raspberry-pi


#http://elinux.org/RPI_vcgencmd_usage
root@raspberrypi:~# \
> for id in core sdram_c sdram_i sdram_p ; do \
>     echo -e "$id:\t$(vcgencmd measure_volts $id)" ; \
> done
core:   volt=1.20V
sdram_c:        volt=1.20V
sdram_i:        volt=1.20V
sdram_p:        volt=1.23V

#Hardware
http://openlabs.co/store/Raspberry-Pi-802.15.4-radio
https://git.openlabs.co/rpi802154.git

