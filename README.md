# Discontinued
If you encounter any issues with this automodder please seek help from ChatGPT or some other AI.

---

# jdu2nx++
A modified version of one of the automodders from c0llydoll/Just-Dance-UbiArt-Nx-Automodder. It takes a codename and coach count and then does the rest!

## Setup Guide
1. Download the .zip from the releases tab and extract it somewhere
2. Install Git & Python (if you haven't already)
3. Run following command in  this directory

```bash
python -m pip install -r requirements.txt
```
4. Set up a Discord account that you'll never touch again (in your browser)
5. Open settings, click "Advanced", and then toggle "Developer Mode"
6. Make a new server on the account
7. Right-click the server, click "Copy Server ID" and paste it into the config as "guild_id"
8. Right-click a channel in the server, click "Copy Channel ID" and paste it into the config as "channel_id"
9. Invite JDH to the server with this link: http://gg.gg/justdancehelper/
10. Go to the server, right-click JDH and just message it anything, you just need to send a message to it once
11. Turn on your bookmarks bar if it isn't there already
12. Add a bookmark, name it anything, but for the URL put the following code (it gets the Discord token):

```javascript
javascript:(function()%7Balert((webpackChunkdiscord_app.push(%5B%5B''%5D%2C%7B%7D%2Ce%3D>%7Bm%3D%5B%5D%3Bfor(let c in e.c)m.push(e.c%5Bc%5D)%7D%5D)%2Cm).find(m%3D>m%3F.exports%3F.default%3F.getToken!%3D%3Dvoid 0).exports.default.getToken())%7D)()%3B
```
13. Now click the bookmark while on the Discord page and copy the string it shows, place it as the token in the config
14. You are done setting it up!
