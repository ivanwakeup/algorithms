'''
python -m flashcards serve [--port 8765]
python -m flashcards add --category caching -q "question" -a "answer" [--source path]
python -m flashcards add --json new_cards.json     # a list of {question, answer, category, source?}
python -m flashcards add --json -                  # same, from stdin
python -m flashcards list [--category caching]
'''
import argparse
import json
import sys
from collections import Counter

from flashcards.server import serve
from flashcards.store import Card, add_cards, load_cards


def cmd_add(args):
    if args.json:
        raw = sys.stdin.read() if args.json == "-" else open(args.json).read()
        new = [Card(question=c["question"], answer=c["answer"], category=c["category"],
                    source=c.get("source", "")) for c in json.loads(raw)]
    else:
        if not (args.question and args.answer and args.category):
            sys.exit("add needs -q, -a and --category (or --json)")
        new = [Card(question=args.question, answer=args.answer, category=args.category,
                    source=args.source or "")]
    added = add_cards(new)
    print(f"added {len(added)} card(s), {len(load_cards())} total")


def cmd_list(args):
    cards = load_cards()
    if args.category:
        cards = [c for c in cards if c.category == args.category]
    for c in cards:
        print(f"[{c.id}] ({c.category}) {c.question}")
    counts = Counter(c.category for c in cards)
    print(f"\n{len(cards)} cards: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))


def main():
    p = argparse.ArgumentParser(prog="flashcards")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("serve")
    s.add_argument("--host", default="127.0.0.1")
    s.add_argument("--port", type=int, default=8765)

    a = sub.add_parser("add")
    a.add_argument("-q", "--question")
    a.add_argument("-a", "--answer")
    a.add_argument("-c", "--category")
    a.add_argument("-s", "--source")
    a.add_argument("--json", help="path to a JSON list of cards, or - for stdin")

    l = sub.add_parser("list")
    l.add_argument("-c", "--category")

    args = p.parse_args()
    if args.cmd == "serve":
        serve(args.host, args.port)
    elif args.cmd == "add":
        cmd_add(args)
    else:
        cmd_list(args)


if __name__ == "__main__":
    main()
