from EpikInteractions import Interface
from quart import Quart, request, jsonify

client = Interface("2e1e645ac21e02cbeba163e7fa5f41ebc0461c15fa26deb6f4775ea6197ac881")

@client.command(
    name = "epikinteraction",
    description = "An EpikInteractions.py Test Command.",
    guild_ids = ["937364424208039957"]
)
async def epikinteraction(interaction):
    await interaction.reply(content="Pong!")

app = Quart(__name__)

@app.post("/")
async def interactions():
    client.process_commands()