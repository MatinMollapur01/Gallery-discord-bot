import discord
from discord.ext import commands
import os  # Add this line to import the 'os' module

# Bot setup with intents
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent
intents.guilds = True  # Enable the guilds intent
intents.message_content = True  # Enable the message content intent
bot = commands.Bot(command_prefix='!', intents=intents)

# Set the directory where images will be stored
IMAGE_DIRECTORY = 'images/'

# Ensure the image directory exists
os.makedirs(IMAGE_DIRECTORY, exist_ok=True)

# Command to upload and save an image
@bot.command(name='upload')
async def upload_image(ctx, image_name: str):
    # Check if an image is attached to the message
    if len(ctx.message.attachments) == 0:
        await ctx.send("No image attached.")
        return

    # Get the first attached image
    image_url = ctx.message.attachments[0].url

    # Download the image and save it with the provided name
    image_path = os.path.join(IMAGE_DIRECTORY, f"{image_name}.png")
    await ctx.message.attachments[0].save(image_path)

    await ctx.send(f"Image '{image_name}' saved successfully!")

# Command to retrieve and send an image
@bot.command(name='getimage')
async def get_image(ctx, image_name: str):
    # Check if the requested image exists
    image_path = os.path.join(IMAGE_DIRECTORY, f"{image_name}.png")
    if os.path.exists(image_path):
        # Send the requested image
        with open(image_path, 'rb') as image_file:
            await ctx.send(file=discord.File(image_file))
    else:
        await ctx.send(f"Image '{image_name}' not found.")

# Run the bot
bot.run('YOUR-TOKEN-HERE')
