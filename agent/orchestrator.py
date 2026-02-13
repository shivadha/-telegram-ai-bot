from agent.memory import get_session, update_state
from tools.url_parser import extract_reel_id
from tools.script_generator import generate_script


async def handle_user_message(user_id, message, telegram_reply):

    session = get_session(user_id)

    # Step 1: Detect Instagram URL
    if "instagram.com" in message:
        reel_id = extract_reel_id(message)

        if reel_id:
            session["data"]["reel_id"] = reel_id
            update_state(user_id, "awaiting_theme")

            await telegram_reply(
                f"🎬 Reel detected!\nReel ID: {reel_id}\n\n"
                "Tell me what you liked about this reel."
            )
        else:
            await telegram_reply("❌ Could not extract reel ID.")

        return

    # Step 2: Awaiting theme description
    if session["state"] == "awaiting_theme":
        session["data"]["theme_description"] = message

        await telegram_reply("🤖 Generating script...")

        script = generate_script(message)

        session["data"]["script"] = script
        update_state(user_id, "awaiting_images")

        await telegram_reply(
            f"✨ Here is your script:\n\n{script}\n\n📸 Now send 2-4 images of Shivit."
        )
        return

    await telegram_reply("Send me an Instagram reel link to start 🚀")
