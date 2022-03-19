from io import BytesIO
import os

from flask import Flask, jsonify, send_file, request

from selenium import webdriver


app = Flask(__name__)


def execute_script(driver: webdriver, x):
    return driver.execute_script("return document.body.parentNode.scroll" + x)


@app.route("/", methods=["GET"])
def default():
    query_params = request.args.to_dict()
    url = query_params.get("url")
    key = query_params.get("key")

    if key != os.getenv("KEY"):
        return jsonify(success="true")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options, executable_path="/home/app/web/chromedriver")
    driver.get(url)

    # width = execute_script(driver, "Width")
    # height = execute_script(driver, "Height")
    driver.set_window_size(800, 800)
    result = driver.find_element_by_tag_name("body").screenshot_as_png
    driver.quit()

    return send_file(BytesIO(result), mimetype="image/png")
