from discord_webhook import DiscordWebhook, DiscordEmbed

from secret import webhookurl

webhook_url = webhookurl.url

webhook = DiscordWebhook(url=webhook_url)

#with open("goku.jpg", "rb") as f:
#    webhook.add_file(file=f.read(), filename='goku.jpg')
with open("goku2.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='goku2.png')

# create embed object for webhook
embed = DiscordEmbed(title='Goku Mode', description='Let\'s get Saiyan', color='fc9803')

# set author (not doing for aesthetics)
#embed.set_author(name='Raghav', url='https://github.com/DogeDevYT', icon_url='https://avatars.githubusercontent.com/u/52612977?v=4')

# set image
embed.set_image(url='attachment://goku2.png')

# set thumbnail (not doing for aesthetics)
#embed.set_thumbnail(url='attachment://goku.jpg')

# set footer (not doing for aesthetics)
#embed.set_footer(text='Will you accept the challenge?', icon_url='attachment://goku.jpg')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name='Part 1', value='100 Push Ups')
embed.add_embed_field(name='Part 2', value='20 Pull ups')

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()