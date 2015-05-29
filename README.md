## Purpose
This simple script allows you to send e-mails via [SMTP](http://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol). Currently, only the non-encryted version (via port 25) is supported. So don't send use this to send confidential information.

## Prerequisites
* Python 2.7+
* The python `config` module (e.g. `sudo pip install config`)

## Getting started
1. Clone the repository via `git clone https://github.com/b3000/mailpy.git`.
2. Copy the file `config.cfg-example` and rename it to `config.cfg` (e.g. `cp config.cfg-example config.cfg` on unix-based systems). Adjust the file to suite your needs and your server configuration.
3. Edit the line `mail(['empfaenger@server.de'], "Betreff", "Nachricht")` in `mail.py` in order to determine recipients, subject and mail content.
4. Send mails via `python mail.py`. This assumes that you `cd`ed into the mailpy dir.
