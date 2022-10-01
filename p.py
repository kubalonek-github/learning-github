@client.event

async def on_message_delete(ctx):

    channel = client.get_channel(1025734128303345734)

    if len(ctx.mentions) == 0:

       





    if len(ctx.mentions) > 0:

        print(ctx.author.name)

        ghostping = discord.Embed(title=f'Wykryto GHOST PING!', color=0xFF0000, timestamp=ctx.created_at)

        ghostping.add_field(name='**Name:**', value=f'{ctx.author.mention} ({ctx.author.id})')

        ghostping.add_field(name='**Usunięta wiadomość:**', value=f'{ctx.content}')

        ghostping.set_thumbnail(

            url='https://bot.to/wp-content/uploads/2020/10/anti-ghost-ping_5f7e1433e80c3.png')

        try:

            await ctx.channel.send(embed=ghostping)

        except discord.Forbidden:

            try:

                await ctx.author.send(embed=ghostping)

            except discord.Forbidden:

                return
