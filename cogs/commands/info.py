
import disnake
from disnake.ext import commands
import variables

infos = commands.option_enum(["logs default", "me", "editor","logs other"])

class info_command(commands.Cog, name='info'):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(title="info",description="Gives you more information about an external feature to improve your datapacking experience")
    async def info(self,inter: disnake.ApplicationCommandInteraction, info: infos):
        if info == "logs default":
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Default Launcher Logs :wood:",
                description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! \nTo open the logs:\n 1. **Enable** logs in the Minecraft **Launcher** \n2. **Start** your **game** (or restart it if you already have an open instance) \n3. Enjoy **spotting errors** getting much **easier**!",
            )
            embed.set_image(
                url="https://media.discordapp.net/attachments/1129493191847071875/1129494068603396096/how-to-logs.png?width=1277&height=897"
            )
        if info == "logs other":
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Other Launcher Logs :wood:",
                description="The logs are where Minecraft displays errors when something goes wrong and can thus help you gain information about why something isn't working for you! Opening logs works different for different 3rd party launchers, here's a quick summary for the most popular ones\n\n**Prism Launcher**\n`Rightclick Instance` > `Edit` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Multi MC**\n`Rightclick Instance` > `Edit Instance` > `Settings` > `Console Settings: Show console while the game is running?`\n\n**Lunar Client**\n`Settings` > `Open Logs in File Exploreer`",
            )

        elif info == "me":
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Datapack Helper <:datapackhelper:1129499893216579614>",
                description="Woah, you are interested in me? :exploding_head: \nWell of course, I would be too! :sunglasses: \nI am a (some would argue the greatest :fire:) bot to help you with everything datapacks! Wether you are looking for a simple template, forgot how to enable the logs or want to know which pack format is the latest, I got you covered! :cold_face: :hot_face:\nAll of this is made possible by the amazing team of Datapack Hub! :duck:",
            )

        elif info == "editor":
            embed = disnake.Embed(
                color=disnake.Color.orange(),
                title="Editor 📝",
                description='While you can make datapacks using any ordinary text editor, our prefered editor of choice is [VSCode](https://code.visualstudio.com/)! \nIt is aviable for Windows, Linux and MacOS (which means it runs on almost all devices) and has lots of great extensions which make the creation of datapacks a whole lot easier!\n\nOur favourite VSCode extensions are:\n[language-mcfunction](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction) - Provides beautiful syntax highlighting for .mcfunction\n[Data-pack Helper Plus](https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server) - Despite how "datapack" is spelled in the title, this adds some really helpful features like auto completion for commands!\n[NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt) - Allows you to view 3D models of your `.nbt` files, directly in VSCode!\n[Datapack Icons](https://marketplace.visualstudio.com/items?itemName=SuperAnt.mc-dp-icons) - Adds cool icons to datapack folders and files',
            )  
       # elif info == "starting out":
       #     embed = disnake.Embed(
       #         color=disnake.Color.orange(),
       #         title="Starting Out 🧒",
       #         description='Here are some tutorials for beginners:\nBasic Datapacking Tutorial by Legitimoose: https://www.youtube.com/watch?v=ac6V5-KT6Rg\nMore uwu',
       #     )
            
        await inter.response.send_message(embed=embed)
        embed = disnake.Embed(
            color=disnake.Colour.orange(),
            title=("**`/info` Command**"),
            description=(str(inter.user.name) + " gained knowledge about `" + info + "`!"),
        )
        channel = self.bot.get_channel(variables.logs)
        await channel.send(embed=embed)