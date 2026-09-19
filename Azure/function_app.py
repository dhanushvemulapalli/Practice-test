import datetime
import json
import threading
import uuid
from typing import Any

import azure.functions as func

app = func.FunctionApp()

# This intentionally lives only for the lifetime of the function worker.
_messages: list[dict[str, Any]] = []
_messages_lock = threading.Lock()


def _json_response(payload: Any, status_code: int = 200) -> func.HttpResponse:
    return func.HttpResponse(
        body=json.dumps(payload),
        status_code=status_code,
        mimetype="application/json",
    )


@app.route(route="message", methods=["POST"], auth_level=func.AuthLevel.ANONYMOUS)
def create_message(req: func.HttpRequest) -> func.HttpResponse:
    """Create and retain a message in this function worker's memory."""
    try:
        body = req.get_json()
    except ValueError:
        return _json_response({"error": "Request body must contain valid JSON."}, 400)

    if not isinstance(body, dict):
        return _json_response({"error": "JSON body must be an object."}, 400)

    content = body.get("content")
    if not isinstance(content, str) or not content.strip():
        return _json_response(
            {"error": "The required 'content' field must be a non-empty string."}, 400
        )

    username = body.get("username")
    if username is not None and not isinstance(username, str):
        return _json_response({"error": "The optional 'username' field must be a string."}, 400)

    message = {
        "id": str(uuid.uuid4()),
        "content": content,
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    if username is not None:
        message["username"] = username

    with _messages_lock:
        _messages.append(message)

    return _json_response(message, 201)


@app.route(route="messages", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def get_messages(req: func.HttpRequest) -> func.HttpResponse:
    """Return all messages retained by this function worker."""
    with _messages_lock:
        messages = list(_messages)
    return _json_response(messages)


@app.route(route="health", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    return _json_response({"status": "Healthy"})
