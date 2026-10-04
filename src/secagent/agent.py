TOOLS = ["scan_env", "report"]
WRITES = ("open security group", "disable auth",)


class InputError(ValueError):
    pass


def run(goal, payload):
    if not isinstance(goal, str) or not goal.strip():
        raise InputError("goal is empty")
    if any(word in goal.lower() for word in WRITES):
        return {"refused": True, "reason": "This agent only reads or plans. It does not write.", "tools": [], "wrote": False, "applied": False}
    env = payload.get("env") or {}; result = [k for k in env if any(p in k.upper() for p in ("PASSWORD", "SECRET", "API_KEY"))]
    return {"refused": False, "tools": TOOLS, "findings": result, "wrote": False, "applied": False}
