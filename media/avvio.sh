#!/usr/bin/env bash


# avvio il virtualenv
workon gse3.6

# mi sposto nella cartella del watchdog e lo avvio in background e in NoHangUp mode
#cd ~/PycharmProjects/watchdog/
nohup python3 watchdog_fotoresize.py &
