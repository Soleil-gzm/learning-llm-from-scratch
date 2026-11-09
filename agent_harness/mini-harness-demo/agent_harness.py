import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).parent
TARGET_FILE = ROOT / "src" / "cart.py"
TRACE_FILE = ROOT / "trace.json"


PATCH_PROPOSAL = '''from decimal import Decimal, ROUND_HALF_UP


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_total(items, user_type="normal"):
    """
    items: [{"price": "60.00", "qty": 2}]
    rules:
    - subtotal >= 100: minus 10
    - vip user: 5% off after threshold discount
    - return Decimal with 2 decimal places
    """
    total = Decimal("0.00")

    for item in items:
        price = Decimal(str(item["price"]))
        qty = int(item["qty"])

        if price < 0:
            raise ValueError("price must not be negative")

        if qty < 0:
            raise ValueError("qty must not be negative")

        total += price * qty

    if total >= Decimal("100.00"):
        total -= Decimal("10.00")

    if user_type == "vip":
        total = total * Decimal("0.95")

    return money(total)
'''


class Harness:
    def __init__(self):
        self.trace = {
            "task": "fix money calculation without float",
            "started_at": datetime.utcnow().isoformat() + "Z",
            "steps": [],
        }

    def log(self, step_type, **kwargs):
        record = {"type": step_type, **kwargs}
        self.trace["steps"].append(record)
        print(json.dumps(record, ensure_ascii=False))

    def run(self, command):
        self.log("run_command", command=command)
        result = subprocess.run(
            command,
            cwd=ROOT,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self.log(
            "command_result",
            exit_code=result.returncode,
            output_tail=result.stdout[-1200:],
        )
        return result.returncode == 0

    def read_file(self, path):
        self.log("read_file", path=str(path.relative_to(ROOT)))
        return path.read_text(encoding="utf-8")

    def write_file(self, path, content):
        allowed = path.resolve() == TARGET_FILE.resolve()
        if not allowed:
            raise PermissionError(f"Not allowed to write {path}")

        self.log("write_file", path=str(path.relative_to(ROOT)))
        path.write_text(content, encoding="utf-8")

    def save_trace(self, status):
        self.trace["finished_at"] = datetime.utcnow().isoformat() + "Z"
        self.trace["final_status"] = status
        TRACE_FILE.write_text(
            json.dumps(self.trace, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def execute(self):
        backup = TARGET_FILE.with_suffix(".py.bak")
        shutil.copyfile(TARGET_FILE, backup)

        try:
            self.read_file(TARGET_FILE)

            baseline_ok = self.run("python -m pytest -q")
            if baseline_ok:
                self.log("baseline", message="tests already pass")
                self.save_trace("already_passed")
                return

            self.write_file(TARGET_FILE, PATCH_PROPOSAL)

            fixed_ok = self.run("python -m pytest -q")
            if not fixed_ok:
                shutil.copyfile(backup, TARGET_FILE)
                self.log("rollback", reason="tests failed after patch")
                self.save_trace("failed_and_rolled_back")
                return

            self.run("python -m py_compile src/cart.py")
            self.log("done", message="patch accepted because tests passed")
            self.save_trace("passed")

        finally:
            if backup.exists():
                backup.unlink()


if __name__ == "__main__":
    Harness().execute()