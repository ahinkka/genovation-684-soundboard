# Genovation 684 soundboard

I programmed the serial connected Genovation controller to output `XX\r\n`
codes where XX is a number index on the controller between 01 and 23
(inclusive). This is then read by the `soundboard.py` script and it plays the
sound files hardcoded in it in a fire and forget manner.

## Installation and running

You'll need a working Python 3 installation and some kind of a serial adapter
to plug the device into.

First install dependencies:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

To run:
```
cp soundboard.ini.sample soundboard.ini # and configure the sounds
./soundboard.ini
```

The script has a working `--help` so that can be used to query its command
line options.

### Runtime dependencies in Debian based distributions (e.g. Raspberry Pi OS)

The following packages should contain all the necessary runtime dependencies:
- python-serial
- sox
- libsox-fmt-all

I.e. running e.g.
```
apt-get install python-serial sox libsox-fmt-all
```
should get you into a state where you can start the program.

## Running MacroMaster684 software in Wine

Requires both proper symlinking in `~/.wine/dosdevices/` and the registry
tricks done as described in https://superuser.com/a/1471614. Otherwise seems
to work fine.

Run the program:
```
wine ~/.wine/drive_c/Program\ Files\ \(x86\)/Genovation/MacroMaster684/MacroMaster684.exe 
```

## Debugging on Linux

The command
```
cu -l /dev/ttyUSB0 -s 9600 -o
```
worked for me after I had added my user into the `dialup` group (and logged in again).

## References

- https://www.genovation.com/downloads/
  - Direct link to MacroMaster684 software: https://www.genovation.com/files/684ver4_30.exe
  - Direct link to 684 manual: https://www.genovation.com/files/684usermanual.pdf

## License

This software is licensed under GPL-3.0 (or later) license. The libraries it
uses are licensed under their own licenses.

License text is available in LICENSE file or from
https://www.gnu.org/licenses/gpl-3.0.txt.
