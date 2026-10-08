import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path

CARDS_PATH = Path(__file__).parent / "cards.json"
CURRENT_PATH = Path(__file__).parent / ".current"  # id of the card on screen; gitignored


@dataclass
class Card:
    question: str
    answer: str
    category: str
    source: str = ""  # where the card came from, e.g. a file path or "session: word ladder"
    id: str = field(default_factory=lambda: uuid.uuid4().hex[:8])
    created: str = field(default_factory=lambda: date.today().isoformat())


def load_cards(path=CARDS_PATH):
    if not path.exists():
        return []
    return [Card(**c) for c in json.loads(path.read_text())]


def save_cards(cards, path=CARDS_PATH):
    path.write_text(json.dumps([asdict(c) for c in cards], indent=2, ensure_ascii=False) + "\n")


def add_cards(new_cards, path=CARDS_PATH):
    cards = load_cards(path)
    existing = {c.question.strip().lower() for c in cards}
    added = []
    for card in new_cards:
        if not card.question.strip() or not card.answer.strip() or not card.category.strip():
            raise ValueError(f"question, answer and category are required: {card}")
        if card.question.strip().lower() in existing:
            print(f"skipping duplicate: {card.question}")
            continue
        existing.add(card.question.strip().lower())
        cards.append(card)
        added.append(card)
    save_cards(cards, path)
    return added


def update_card(card_id, question, answer, path=CARDS_PATH):
    if not question.strip() or not answer.strip():
        raise ValueError("question and answer are required")
    cards = load_cards(path)
    for card in cards:
        if card.id == card_id:
            card.question, card.answer = question, answer
            save_cards(cards, path)
            return card
    return None


def set_current(card_id, path=CURRENT_PATH):
    path.write_text(card_id)


def get_current(path=CURRENT_PATH, cards_path=CARDS_PATH):
    if not path.exists():
        return None
    card_id = path.read_text().strip()
    return next((c for c in load_cards(cards_path) if c.id == card_id), None)


def delete_card(card_id, path=CARDS_PATH):
    cards = load_cards(path)
    remaining = [c for c in cards if c.id != card_id]
    if len(remaining) == len(cards):
        return False
    save_cards(remaining, path)
    return True
