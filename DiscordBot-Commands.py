# Leak Lookup. (RIP Scylla)

@bot.command()
async def leaklookup(self, query):
    confirmation = BotConfirmation( self, 0x012345 )
    await confirmation.confirm( f"Continuing Searching This Email: {query}?" )

    if confirmation.confirmed:
        await confirmation.update( "Searching!", color=0x55ff55 )
        r = requests.get( f"https://scylla.so/search?q=email:{query}size=100&start=200", verify=False, headers={'Accept': 'application/json'} )
        ipinfo = BeautifulSoup( r.content, "html.parser" )
        strIpinfo = str( ipinfo ).replace( "}},", "\n" )

        text_file = open( f"{query}.txt", "w" )
        text_file.write( 'DB Search Tool - w00dy. \n' )
        text_file.write( f'{strIpinfo}' )
        text_file.close()

        await asyncio.sleep( 3 )
        await self.channel.purge( limit=2 )
        await self.send( file=discord.File( rf'{query}.txt' ) )
        os.remove( f"{query}.txt" )
    else:
        await confirmation.update( "Bailed!", hide_author=True, color=0xff5555 )
        await self.channel.purge( limit=2 )
        return
      
      
# CFX Resolver.      
@bot.command()
async def CFX(self, ip):
    ipopen = requests.get("https://api.lea.kz/cfx.php?cfxres=" + ip + "&key=FBI-BENNETTCHANGED")
    openinfo = ipopen.json()

    backend = openinfo["Backend"]
    players = openinfo["Players"]
    owner = openinfo["Owner"]

    sent = discord.Embed( title=f"CFX Resolver :shield:", color=0x000000 )
    sent.add_field( name="Backend:", value=f"```{backend}```", inline=False )
    sent.add_field( name="Players:", value=f"```{players}```", inline=False )
    sent.add_field( name="Owner: ", value=f"```{owner}```", inline=False )

    await self.channel.send(embed=sent)

# Offline Or Online?
@bot.command()
async def ping(self, ip):
    p = os.system( "ping " + ip )

    if (p == 0):
        embed = discord.Embed(
            title='ONLINE',
            colour=discord.Colour.green()
        )
        embed.set_image( url='https://i.pinimg.com/originals/80/32/6c/80326c84c6e00910f63aa6260372ec25.gif' )
        await self.channel.send( embed=embed )
    else:
        embed = discord.Embed(
            title='OFFLINE',
            colour=discord.Colour.red()
        )
        embed.set_image( url='https://miro.medium.com/max/1600/1*bdIZoSioXqIAl8gw27E_xA.gif' )
        await self.channel.send( embed=embed )

