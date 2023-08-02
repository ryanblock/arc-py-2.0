from platform import python_version as ver
import arc


def handler(req, context):
    session = arc.http.session_read(req)
    if session.get("count") is None:
        session["count"] = 0
    else:
        session["count"] += 1

    json = {"ok": True, "runtime": f"Python v{ver()}", "count": session["count"]}
    # As in Node.js @architect/functions, including a `sessions` property in your response will automatically record the latest session data
    response = {"session": session, "json": json}
    return arc.http.res(req, response)
