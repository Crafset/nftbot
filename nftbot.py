import discord
import requests
import asyncio

source_guild_id = "1046516981907591279"  # Remplacez "ID_DU_SERVEUR_SOURCE" par l'ID réel du serveur source
category_id = "1091438158404649091"  # Remplacez "ID_DE_LA_CATEGORIE" par l'ID réel de la catégorie
webhook_url = "URL_DU_WEBHOOK"  # Remplacez "URL_DU_WEBHOOK" par l'URL réelle du webhook de votre serveur Discord

class MyClient(discord.Client):
    async def on_guild_channel_create(self, channel):
        if isinstance(channel, discord.TextChannel) and channel.guild.id == source_guild_id and channel.category_id == category_id:
            await asyncio.sleep(300)  # Attendre 5 minutes (300 secondes)
            messages = await channel.history(limit=1).flatten()  # Récupérer le dernier message du salon
            if messages:
                message = messages[0]
                embed = discord.Embed(
                    title=f"Nouveau salon créé : {channel.name}",
                    description=f"Contenu initial : {message.content}",
                    color=discord.Color.green()
                )
                payload = {
                    "embeds": [embed.to_dict()]
                }
                requests.post(webhook_url, json=payload)

client = MyClient()
client.run()  # Pas besoin de spécifier le jeton (token) du bot
