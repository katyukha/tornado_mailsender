To install just do:

```bash
    $ pip install -e https://github.com/katyukha/tornado_mailsender.git
```

Or

```bash
    $ git clone https://github.com/katyukha/tornado_mailsender.git
    $ cd tornado_mailsender
    $ python setup.py install
```

This is a simple web server with aming only to send emails.
Server side configuration is done via command line arguments passed to a server.

After install to see all available options just call:

```bash
    $ tornado_mailsender_server --help
```

To send mail via this server just make post request to URL */send_mail/*
To get information on what data shoud be supplied to POST request, just do
GET request to that address.

