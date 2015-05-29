import sys, os, re
#from smtplib import SMTPDSSL as SMTP # port 465, encryption
from smtplib import SMTP    # port 25, no encryption
from email.MIMEText import MIMEText
from config import Config

def mail(des, sub, msg):
    try:
        f = file('config.cfg')
        cfg = Config(f)

        message = MIMEText(msg, cfg.txt)
        message['Subject']= sub
        message['From']   = cfg.mail
                            
        conn = SMTP(cfg.server)
        conn.set_debuglevel(False)
        conn.login(cfg.user, cfg.pw)

        try:
            conn.sendmail(cfg.mail, des, message.as_string())
        finally:
            conn.close()
    
    except Exception, exc:
        sys.exit( "mail failed; %s" % str(exc) ) # Error message  

mail(['empfaenger@server.de'], "Betreff", "Nachricht")
