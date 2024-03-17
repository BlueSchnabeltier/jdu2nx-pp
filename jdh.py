from time import sleep
from discum import Client
from discum.utils.slash import SlashCommander

class JDHClient:
    def __init__(self, token: str, guild_id: str, channel_id: str, bot_id: str = "755796344865685625", edit_delay: int = 3):
        self.__bot_id = bot_id
        self.__client = Client(token=token, log=False)
        self.__guild_id = guild_id
        self.__channel_id = channel_id
        self.__edit_delay = edit_delay

    def __remove_from_string(self, string: str, substrings: list):
        for substring in substrings:
            string = string.replace(substring, "")

        return string

    def get_nohud(self, codename: str):
        commands = self.__client.getSlashCommands(self.__bot_id).json()
        slash_commander = SlashCommander(commands)
        data = slash_commander.get(["nohud"], inputs={"codename": codename})

        self.__client.triggerSlashCommand(self.__bot_id, channelID=self.__channel_id, guildID=self.__guild_id, data=data)
        sleep(self.__edit_delay)

        nohuds = {}
        message = self.__client.getMessages(channelID=self.__channel_id).json()[0]
        fields = message["embeds"][0]["fields"]

        for field in fields:
            name = self.__remove_from_string(field["name"], [":"]).lower().replace(" ", "_")
            value = self.__remove_from_string(field["value"], ["[Link]", "(", ")"])
            nohuds[name] = value

        return nohuds