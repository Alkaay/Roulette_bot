def runn_webhook(bot):
    from flask import Flask, abort, request
    from config import outer_ip, token
    import telebot
    import time

    app = Flask(__name__)

    # Process webhook calls
    WEBHOOK_HOST = outer_ip  # outer ip
    WEBHOOK_PORT = 443  # 443, 80, 88 or 8443 (port need to be 'open')
    WEBHOOK_LISTEN = outer_ip  # in some VPS you may need to put here the IP addr

    WEBHOOK_SSL_CERT = '/home/frizon1993/webhook_cert.pem'  # path to the ssl certificate
    WEBHOOK_SSL_PRIV = '/home/frizon1993/webhook_pkey.pem'  # path to the ssl private key

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (token)

    @app.route(WEBHOOK_URL_PATH, methods=['POST'])
    def webhook():
        if request.headers.get('content-type') == 'application/json':
            json_string = request.get_data().decode('utf-8')
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_updates([update])
            return ''
        else:
            abort(403)

    bot.remove_webhook()
    time.sleep(0.1)
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))
    app.run(host=WEBHOOK_LISTEN,
            port=WEBHOOK_PORT,
            ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
            )  # debug=True)
