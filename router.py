from flask import Flask, url_for, render_template, request
import requests
from bs4 import BeautifulSoup, Tag

import HTMLParser


from js_payload import payload

app = Flask(__name__)

app.debug = True
app.restart = True


@app.route('/submission', methods=["POST"])
def submission():
	html = request.form['annotated_html']

	parser = HTMLParser.HTMLParser()

	decoded_html = parser.unescape(html)

	bs_decoded = BeautifulSoup(html)


	print bs_decoded
	# print decoded_html


	

@app.route('/', methods=["GET", "POST"])
def home():
	if request.method == "GET":
		return render_template("scrapermaker_form.html")

	elif request.method == "POST":
		url = request.form['url']
		r = requests.get(url)
		bs = BeautifulSoup(r.content)
		js_tag = Tag(bs, name="script")


		js_tag.string = payload
		body = bs.find("body")
		body.append(js_tag)

		return str(bs)





if __name__ == "__main__":
	app.run(port=9000)
