#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornado.options import options, define

import smtplib
from email.mime.text import MIMEText

# defines
define('port', type=int, default=8888)
define('host', type=str, default='localhost')
define('email_host', type=str)
define('email_port', type=int)
define('email_tls', type=bool, default=True)
define('email_username', type=str)
define('email_password', type=str)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Make post request to this URL to send mail.<br/>")
        self.write("You should provide next field in POST request:<bt/>")
        self.write("<ul><li>email_from</li><li>email_to</li><li>email_subject</li><li>email_body</li></ul><br/>")
        self.write("Note that 'email_to' field may be passed few times in one request<br/><br/>")
        self.write("""
              <form method="POST">
                   <h6>Test form. Enter ddata here to check if email would be sent</h6>
                   Email from: <input name="email_from"/><br/>
                   Email to: <input name="email_to"/><br/>
                   Email Subject: <input name="email_subject"/><br/>
                   Email Body: <textarea name="email_body"></textarea><br/>
                   <button type="submit">Send!</button>
              </form>
        """)

    def post(self):
        connection = smtplib.SMTP(options.email_host,
                                  options.email_port)

        if options.email_tls:
            connection.ehlo()
            connection.starttls()
            connection.ehlo()

        if options.email_username and options.email_password:
            connection.login(options.email_username, options.email_password)

        msg = MIMEText(self.get_argument('email_body'))
        msg['From'] = email_from = self.get_argument('email_from')
        email_to = self.get_arguments('email_to')
        msg['To'] = u', '.join(email_to)
        msg['Subject'] = self.get_argument('email_subject')
        connection.sendmail(email_from, email_to, msg.as_string())
        connection.quit()
        self.write("OK")


if __name__ == "__main__":
    options.parse_command_line()

    handlers = [
        (r"/send_mail/", MainHandler),
    ]
    application = tornado.web.Application(handlers)

    application.listen(options.port, options.host)
    tornado.ioloop.IOLoop.instance().start()
