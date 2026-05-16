import os

from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


def _public_base_url() -> str:
    """Canonical site origin for Open Graph URLs (must be absolute https in production).

    Set PUBLIC_BASE_URL=https://your-domain.com when behind a reverse proxy so
    share previews use the public URL rather than an internal http host.
    """
    env = os.environ.get("PUBLIC_BASE_URL", "").strip().rstrip("/")
    if env:
        return env
    return request.url_root.rstrip("/")


@app.route("/")
def home():
    base = _public_base_url()
    return render_template(
        "index.html",
        canonical_url=f"{base}/",
        og_title="To my Mom",
        og_description="Happy birthday — a heartfelt letter from Jayda.",
        og_image_url=f"{base}/img/heart-svgrepo-com.png",
        og_image_width=1024,
        og_image_height=1024,
    )

@app.route("/img/<filename>")
def img_file(filename):
    return send_from_directory('img', filename)

if __name__ == "__main__":
    app.run()