import asyncio

import os

import apprise

from config import *

import database

async def check_cards_notify():
    with session_scope() as session:
    	cards = database.get_cards(session)
    for card in cards:
        online_card = account.get_card(card.number)
        if card.notified == False:
            if online_card.pending > 0:
                apobj = apprise.Apprise()
                apobj.add(APPRISE_EMAIL_URL.format(email_to=card.email))
                await apobj.async_notify(
                title="Payback for Xente Nova ready!",
                body=f"Now you can go to your nearest ABANCA ATM to get a refund of your latest trips with the Xente Nova card, a total of {online_card.pending}€.",
                )

                card.notified = True
                session.commit()
        else:
            if online_card.pending == 0:
                card.notified = False
                session.commit()

async def main():
    while True:
        asyncio.create_task(check_cards_notify())
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    asyncio.run(main())
