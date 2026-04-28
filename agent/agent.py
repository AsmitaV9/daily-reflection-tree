import csv

TREE_FILE = "../tree/reflection-tree.tsv"


class Node:
    def __init__(self, row):
        self.id = row["id"]
        self.parent = row["parentId"]
        self.type = row["type"]
        self.text = row["text"]
        self.options = row["options"].split("|") if row["options"] else []
        self.target = row["target"]
        self.signal = row["signal"].split("|") if row["signal"] else []


def load_tree():
    nodes = {}
    children = {}

    with open(TREE_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            node = Node(row)
            nodes[node.id] = node

            if node.parent:
                children.setdefault(node.parent, []).append(node.id)

    return nodes, children


def interpolate(text, answers):
    for qid, ans in answers.items():
        placeholder = "{" + qid + ".answer}"
        text = text.replace(placeholder, ans)
    return text


def run():
    nodes, children = load_tree()
    current = nodes["START"]

    answers = {}
    axis_signals = {"axis1": 0, "axis2": 0, "axis3": 0}

    while True:
        print("\n" + "-" * 60)
        print(interpolate(current.text, answers))

        if current.type == "end":
            break

        # ---------------- QUESTION ----------------
        elif current.type == "question":
            for i, option in enumerate(current.options):
                print(f"{i + 1}. {option}")

            choice = int(input("Choose an option: ")) - 1
            answers[current.id] = current.options[choice]

            # Per-option signal handling
            if current.signal and choice < len(current.signal):
                sig = current.signal[choice]
                if ":" in sig:
                    axis, _ = sig.split(":")
                    axis_signals[axis] += 1

            # Move to child
            next_ids = children.get(current.id, [])
            current = nodes[next_ids[0]] if next_ids else None

        # ---------------- DECISION ----------------
        elif current.type == "decision":
            next_ids = children.get(current.id, [])

            if len(next_ids) >= 2:
                # Decide axis from node id
                if "A1" in current.id:
                    axis = "axis1"
                elif "A2" in current.id:
                    axis = "axis2"
                elif "A3" in current.id:
                    axis = "axis3"
                else:
                    axis = None

                if axis and axis_signals[axis] >= 2:
                    current = nodes[next_ids[0]]
                else:
                    current = nodes[next_ids[1]]
            else:
                current = nodes[next_ids[0]] if next_ids else None

        # ---------------- REFLECTION / START ----------------
        elif current.type in ["reflection", "start"]:
            next_ids = children.get(current.id, [])
            current = nodes[next_ids[0]] if next_ids else None

        # ---------------- BRIDGE ----------------
        elif current.type == "bridge":
            current = nodes[current.target]

        # ---------------- SUMMARY ----------------
        elif current.type == "summary":
            summary_text = interpolate(current.text, answers)
            print(summary_text)
            next_ids = children.get(current.id, [])
            current = nodes[next_ids[0]] if next_ids else None

        if current is None:
            break

    print("\nSession complete.\n")
    print("Axis signals:", axis_signals)


if __name__ == "__main__":
    run()