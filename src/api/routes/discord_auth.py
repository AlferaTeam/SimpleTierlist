from fastapi import APIRouter

from src.services.discord import DiscordOAuthClient
from src.settings import discord

router = APIRouter()
discord_client = DiscordOAuthClient(discord.CLIENT_ID, discord.CLIENT_SECRET, discord.REDIRECT_URL)


@router.get('/login')
async def start_login():
    return discord_client.redirect()


@router.get('/callback')
async def finish_login(code: str):
    user = await discord_client.login(code)
    print(user)
    return user
