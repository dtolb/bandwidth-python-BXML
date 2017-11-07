<div align="center">

# bandwidth-python-BXML

<img src="https://s3.amazonaws.com/bwdemos/BW_Voice.png"/>
Simple Quickstart for Bandwidth and Python 3 using Flask and BXML
</div>

## Pre-reqs

* [Bandwidth Account](http://dev.bandwidth.com)
* [ngrok](https://ngrok.com/) Installed with account
* [Python 3](https://www.python.org/downloads/)
* [VirtualEnv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [Bandwidth Phone Number](http://dev.bandwidth.com/howto/buytn.html)

## Setup Environment Variables

> [How to setup environment variables](https://www.schrodinger.com/kb/1842)

| Environment Variable   | Description                                                    | Example                |
|:-----------------------|:---------------------------------------------------------------|:-----------------------|
| `BANDWIDTH_USER_ID`    | [Bandwidth USER Id](http://dev.bandwidth.com/security.html)    | `u-123sdaf9834sd`      |
| `BANDWIDTH_API_TOKEN`  | [Bandwidth API Token](http://dev.bandwidth.com/security.html)  | `t-asdg920358askdf`    |
| `BANDWIDTH_API_SECRET` | [Bandwidth API Secret](http://dev.bandwidth.com/security.html) | `asdfkljasd2305jsdlkf` |

## Installation

### Clone this repo

```bash
git clone https://github.com/dtolb/bandwidth-python-BXML.git

cd bandwidth-python-BXML
```


### Create [Virtual Environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```bash
virtualenv -p {location_of_python3} bandwidth-python-BXML

source bandwidth-python-BXML/bin/activate
```

❗❗❗ When you're done be sure to `deactivate` ❗❗❗

```bash
deactivate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Launch the App

```bash
FLASK_APP=app.py flask run
```

### Setup with ngrok

[Ngrok](https://ngrok.com) is an awesome tool that lets you open up local ports to the internet.

Once you have ngrok installed, open a new terminal tab and navigate to it's location on the file system and run:

```bash
./ngrok http 5000
```

You'll see the terminal show you information

![ngrok terminal](https://s3.amazonaws.com/bw-demo/ngrok_terminal.png)

### Update `app.py`

Copy your ngrok information and bandwidth phone number to [app.py](app.py)

```python
bw_from_number = ''
your_server_url = ''
```

### 👍👍 Then create a `POST` request to your URL to initiate the flow

```http
POST http://your_server.com/create-verification-call HTTP/1.1
Content-Type: application/json; charset=utf-8

{
  "phoneNumber": "+15554443333"
}
```

