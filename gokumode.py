from discord_webhook import DiscordWebhook, DiscordEmbed

from secret import webhookurl

webhook_url = webhookurl.url

#long boi content thing a ding is role id for goku-mode
webhook = DiscordWebhook(url=webhook_url, content="Allright Saiyans, lets see if you're up for an AB ATTACK!!!!")

#with open("goku.jpg", "rb") as f:
#    webhook.add_file(file=f.read(), filename='goku.jpg')
with open("goku4.png", "rb") as f:
    webhook.add_file(file=f.read(), filename='goku4.png')

# create embed object for webhook
embed = DiscordEmbed(title='Goku Mode', description='AB ATTACK', color='fc9803')

# set author (not doing for aesthetics)
#embed.set_author(name='Raghav', url='https://github.com/DogeDevYT', icon_url='https://avatars.githubusercontent.com/u/52612977?v=4')

# set image
embed.set_image(url='attachment://goku4.png')

# set thumbnail (not doing for aesthetics)
#embed.set_thumbnail(url='attachment://goku.jpg')

# set footer (not doing for aesthetics)
#embed.set_footer(text='Will you accept the challenge?', icon_url='attachment://goku.jpg')

# set timestamp (default is now)
embed.set_timestamp()

# add fields to embed
embed.add_embed_field(name='Part 1', value='1 Minute Hollow Body Hold')
embed.add_embed_field(name='Hollow Body Hold Guide', value='https://www.verywellfit.com/how-to-do-a-hollow-body-hold-techniques-benefits-variations-5079591')
embed.add_embed_field(name='Part 2', value='30 seconds of Russian twists')
embed.add_embed_field(name='Russian Twists Guide', value='https://www.youtube.com/watch?v=wkD8rjkodUI')
embed.add_embed_field(name='Part 3', value='30 seconds of side planks (each side)')


# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()