from flask import Blueprint, request

from .tasks import i

bp = Blueprint('bp', __name__)

@bp.route("/api", methods = ["POST"])
def api():
    content = request.json 
    task = i.delay(content) #register context in the db, no return since task not ready 
    return "ok"

@bp.route("/", methods = ["GET"])
def hello_world():
    return "hello, world"

# new comment

