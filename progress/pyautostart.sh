#! /bin/sh
### BEGIN INIT INFO
# Provides: RGB_Printer.py
# Required-Start: $syslog
# Required-Stop: $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start LED/ RGB Application
# Description: Ersell wurde ein python script, welches den 3D Drucker zum leuchten 
#bringen soll, und später aktuelle Statusmeldungen anzeigt
### END INIT INFO
 
case "$1" in
    start)
        echo "RGB Stripe wird gestartet"
        # Starte Programm
        /usr/local/bin/RGB_Printer.py
        ;;
    stop)
        echo "RGB Stripe wird ausgeschaltet"
        # Beende Programm
        killall RGB_Printer.py
        ;;
    *)
        echo "Benutzt: /etc/init.d/RGB_Printer.py {start|stop}"
        exit 1
        ;;
esac
 
exit 0