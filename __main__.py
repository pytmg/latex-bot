import os, discord, matplotlib.pyplot as plt, io
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def latex_to_png(latex: str) -> io.BytesIO:
    fig = plt.figure()
    fig.patch.set_alpha(0)

    # render text first
    text = plt.text(0, 0, f"${latex}$", fontsize=40, color="white")

    # draw to get bbox
    fig.canvas.draw()
    bbox = text.get_window_extent()

    # convert bbox to inches
    dpi = 300
    width, height = bbox.width / dpi, bbox.height / dpi

    # resize figure to fit text exactly
    fig.set_size_inches(width, height)

    # reposition text properly
    text.set_position((0, 0))

    plt.axis("off")

    buf = io.BytesIO()
    plt.savefig(
        buf,
        format="png",
        dpi=dpi,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0.0
    )
    plt.close(fig)

    buf.seek(0)
    return buf

@bot.tree.command(name="latex", description="Create a LaTeX text")
async def latexcmd(interaction: discord.Interaction, latex: str):
    try:
        img = latex_to_png(latex)
        file = discord.File(img, filename="latex.png")
        await interaction.response.send_message(file=file)
    except Exception as e:
        await interaction.response.send_message(f"error: {e}", ephemeral=True)

@bot.event
async def on_ready():
    cmds = await bot.tree.sync()
    print(f"Synced {len(cmds)} commands")
    print(f"Logged in as {bot.user.name}")

bot.run(TOKEN)