# Empty Bot

```python
import discord

client = discord.Client()

# features

client.run('token')

```

# Features

## Events


## Commands

Commands have generally 3 aspects to consider, (1) the context of their invocation, (2) their interface and (3) their logic.

To register a command we need first to define a prefix ot which the bot will answer.

````python
from discord.ext import commands

bot = commands.Bot(command_prefix='prefix')

````

There are two ways to register a command.

One, using the decorator.

``````python

@bot.command()
async def handler(context):
    pass

``````
Two, using the .add_command method.

```python

@commands.command()
async def handler(context):
    pass
    
bot.add_command(handler)

```

Since both are equivalent and the first method is neater, it will be the default go for defining commands.

### arguments
All that is typed - space-separated words - after the command is considered an argument to be passed to the handler.

```python
@bot.command()
async def handler(context, arg1, arg2, ...):
    # captures arguments positionally
    pass

@bot.command()
async def handler(context, *args):
    # captures all the arguments in <args>:list.
    pass
    
```

### context
A command handler must at least have the `context` argument. The variable contains information revelant to where the command was issued, namely the context. 

```codithm

context : {

    .author // name of the author
    .guild // name of the server
    .channel // an object representing the channel

    .send() // messages the answer to the command

}

```

### conveters
Converters are used to transform an argument received by a command to a target type. 

They can be specified using *function annotations*. 

````python

def converter(arg):
    # result <- ( arg -> transformation )
    return result

@bot.command()
async def handler(ctx, arg: converter):
    pass

````

Discord.py comes with the `Conveter` interface to define custom converters beside the one shipped with the package.

```python

from discord.ext import commands

class CustomConverter(commands.Converter):

    async def convert(self, context, arg):
        # result <- ( arg -> transformation )
        return result
# OR

class CustomConverter(commands.Converter):
    def __init__(self, arg):
        # self._state <- arg

    @classMethod
    async def convert(self, arg):
        # result <- ( arg -> transformation )
        return result

    @property
    def prop(self):
        return # something about the _state


@bot.command()
async def handler(ctx, arg: """CustomConverter OR CustomConverter()"""):
    # Having the possibility of the converter be constructed allows you to set up some state in the converter’s __init__ for fine tuning the converter.
    pass

```
Built-in converters, `UserConverter`, `MemberConverter`, `MessageConverter`, `TextChannelConverter`, `VoiceChannelConverter`, `StageChannelConverter`, `StoreChannelConverter`, `CategoryChannelConverter`, `EmojiConverter`, `GuildConverter`, `RoleConverter`.

We can make the conversion logic richer by using `typing`'s `.Union` and `.Optional`.
