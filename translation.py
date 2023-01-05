from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
This command is used to short or convert links from first to last posts

Make the bot as an admin in your channel

Command usage: `/batch [channel id or username]`

Ex: `/batch -100xxx`
"""

START_MESSAGE = '''**Hello, {}
\nI Am [IndiURL Bot](https://t.me/Indiurl), Bulk Link Converter. I Can Convert Links Directly From Your [IndiURL](https://indiurl.in.net/auth/signin) Account,
    
1. Go To 👉 https://indiurl.in.net/member/tools/api
2. Then Copy API Key
3. Then Type /shortener_api than give a single space and then paste your API Key. 

» Example👇**
/shortener_api cbd63775f798fe6e58c67a56e6ce8b70c495cda4

<b>» Commands :
/help : To Get Help.
/footer : To Get Help About Adding your Custom Footer to bot.
/header : To Get Help About Adding your Custom Footer to bot.</b>'''



HELP_MESSAGE = '''
**Hey! My name is {firstname}. I am a IndiURL Shortener Bot.**

**» Features :**
• [Hyperlink](https://t.me/{username})
• Buttons convert support
• Header and Footer Text support
• Replace Username
• Banner Image
\n**» Helpful commands:**
/start: Starts me!
/help: Sends this message; I'll tell you more about myself!
\nIf You Have Any Problem Then Contact Our [Support.](https://t.me/priyanshuu11)
\n**» Available commands:**
/shortener_api
/header
/footer
/username
/banner_image
/me

**Use the commands to know more about my features.**'''



ABOUT_TEXT = """
**» My Details:**
**• Name:** ** {} **  
**• Owner :** <a href=https://t.me/priyanshuu11 ><b>Support</b></a>
**• Updates:**` <a href=https://t.me/IndiURL ><b>IndiURL</b></a>
"""


METHOD_MESSAGE = """
Current Method: {method}
    
Methods Available:

> `mdlink` - Change all the links of the post to your MDisk account first and then short to {shortener} link.

> `shortener` - Short all the links of the post to {shortener} link directly.

> `mdisk` - Save all the links of the post to your Mdisk account.
    
To change method, choose it from the following options:
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, Send in this format 👇
`[link]` | `[custom_alias]`

Ex: https://t.me/example | Example

**» This feature works only in private mode only**"""


ADMINS_MESSAGE = """
»List of Admins :
1. {admin_list}
"""


CHANNELS_LIST_MESSAGE = """
List of channels that have access to this Bot:

{channels}"""

HELP_REPLY_MARKUP = InlineKeyboardMarkup([

    [
        InlineKeyboardButton('Custom Alias', callback_data=f'alias_conf'),
        InlineKeyboardButton('Admins', callback_data=f'admins_list'),    
    ],

    [
        
        #InlineKeyboardButton('Channels', callback_data=f'channels_list'),
        InlineKeyboardButton('Home', callback_data='start_command')
        
    ],


])


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Home', callback_data=f'start_command'),
        InlineKeyboardButton('Help', callback_data=f'help_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

START_MESSAGE_REPLY_MARKUP  = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Help', callback_data=f'help_command'),
        InlineKeyboardButton('About', callback_data='about_command')
    ],
    [
        InlineKeyboardButton('Close', callback_data='delete')
    ]
])

METHOD_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Shortener', callback_data=f'change_method#TnlinksWithMdisk'),
        InlineKeyboardButton('Shortener', callback_data='change_method#Tnlinks')
    ],
        [
        InlineKeyboardButton('Back', callback_data=f'help_command'),
        InlineKeyboardButton('Close', callback_data='delete')
    ],

])

BACK_REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('Back', callback_data=f'help_command')
    ],

])

USER_ABOUT_MESSAGE = """

- Header Text: 
{header_text}

- Footer Text: 
{footer_text}

- Banner Image: {banner_image}
"""


MDISK_API_MESSAGE = """Mdisk Not Supports."""

SHORTENER_API_MESSAGE = """To add or update your Shortner Website API, 
`/shortener_api [api]`
            
Ex: `/shortener_api test`
"""

HEADER_MESSAGE = """Reply to the Header Text You Want

This Text will be added to the top of every message caption or text

For adding line break use \\n

To Remove Header Text: `/header remove`"""

FOOTER_MESSAGE = """Reply to the Footer Text You Want

This Text will be added to the bottom of every message caption or text

For adding line break use \\n

To Remove Footer Text: `/footer remove`"""

USERNAME_TEXT = """Current Username: {username}

Usage: `/username your_username` (without @)

This username will be automatically replaced with other usernames in the post

To remove this username, `/username remove`"""

BANNER_IMAGE = """
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
