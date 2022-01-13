from .models import Base, Card

def get_card(session, number):
    card = (
        session.query(Card)
        .filter(Card.number == number)
        .one_or_none()
    )

    return card

def get_cards(session):
    cards = (
        session.query(Card).all()
    )

    return cards

def add_card(session, number, email):
    card = Card(number=number, email=email, notified=False)
    session.add(card)

    session.commit()

def delete_card(session, number):
    card = get_card(session, number)
    if card is None:
        return False

    session.delete(card)

    session.commit()
    return True
