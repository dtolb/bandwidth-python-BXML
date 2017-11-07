import os
import sys
import pprint
import json

from bw_clients import *
from flask import Flask, request, render_template, Response

app = Flask(__name__)

def po(o):
    """
    Prints things to console much more nicely than the default print
    """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(o)

# Global variable for app name
bw_from_number = ''
your_server_url = ''

@app.route('/create-verification-call', methods=['POST'])
def handle_create_verification():
  """
  Setup a handler to post to create a verification call
  """
  verification_request = request.get_json()
  po(verification_request)
  callback_url = your_server_url + '/outbound-voice-callbacks'
  # Get the phone number to verify
  verify_phone_number = verification_request['phoneNumber']
  call_id = voice_api.create_call(from_=bw_from_number,
                                to=verify_phone_number,
                                callback_timeout='6000',
                                callback_url=callback_url, ## Set this to your server's url and endpoint
                                callback_http_method='GET' ##Set this to GET to use BXML
                                )

  return Response(response="Creating verification call", status=201)

@app.route('/outbound-voice-callbacks', methods=['GET'])
def handle_voice():
    """
    Setup a callback handler for GET voice events
    """

    # Get the event type

    event_type = request.args.get('eventType')
    po(event_type)

    # here we go, call is answered
    if event_type == 'answer':

        # Speak Sentence
        sentence = "Your verification code for the Kinney Drugs pharmacy portal is " \
        "1 2 3 4 5 6. If you did not initiate this request there is " \
        "nothing you need to do. To complete verifying your identity and " \
        "start managing your prescriptions online, your " \
        "verification code to enter is 1 2 3 4 5 6."

        bxml = '<?xml version="1.0" encoding="UTF-8"?>' \
        '<Response>' \
        '<SpeakSentence gender="female" voice="julie">%s</SpeakSentence>' \
        '<Hangup/>' \
        '</Response>' % sentence

        po(bxml)
        r = Response(response=bxml, status=200)
        r.headers["Content-Type"] = "application/xml; charset=utf-8"
        return r

    else:
        # Ignore everything else
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}