import os

import disnake
import dph
from disnake.ext import commands
from aiofiles import open

methods = os.listdir("./method")

for idx, ele in enumerate(methods):
    methods[idx] = ele.replace(".md", "")

MethodsType = commands.option_enum(methods)


class MethodCommand(commands.Cog, name="method"):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(
        title="method",
        description="Shows information about methods commonly used in datapacks",
    )
    async def method(
        self, inter: disnake.ApplicationCommandInteraction, method: MethodsType
    ):
        async with open("./method/" + str(method) + ".md") as opened_file:
            file_content = await opened_file.read()
            
        text = f"""# {method.title()}
        >>> {file_content}"""

        await inter.response.send_message(text)

        await dph.log("`/method` Command", f"A user looked up the `{method}` method","orange",self)
