-- NextHub Legacy Loader
local Players     = game:GetService("Players")
local StarterGui  = game:GetService("StarterGui")
local LocalPlayer = Players.LocalPlayer

local DISCORD_URL = "https://discord.gg/hJayhS9ZYZ"

local MESSAGE = string.format([[
⚠️ NextHub: This Loader Is No Longer Active!

The old loader has been removed. 
Please join our Discord server and get the latest loader.

Discord: %s
]], DISCORD_URL)

pcall(function()
    StarterGui:SetCore("SendNotification", {
        Title    = "NextHub - Update Required",
        Text     = "This loader is no longer active!",
        Duration = 8,
    })
end)

task.wait(3)

LocalPlayer:Kick(MESSAGE)