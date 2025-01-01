hi im exploimarker or Sasha im 🇷🇺
I use chat gpt to create scripts
and I'm interested in programming languages like Lua,java, python,c#,c++. Don't hate my scripts. I just started writing scripts.
here is my script, which is still in development:https:local TweenService = game:GetService("TweenService")
local Players = game:GetService("Players")
local function createUICorner(parent, cornerRadius)
    local uiCorner = Instance.new("UICorner")
    uiCorner.CornerRadius = UDim.new(0, cornerRadius)
    uiCorner.Parent = parent
end

local function createButton(parent, text, position, size, color, textColor, callback)
    local button = Instance.new("TextButton")
    button.Parent = parent
    button.Text = text
    button.Position = position
    button.Size = size
    button.BackgroundColor3 = color
    button.TextColor3 = textColor
    createUICorner(button, 15)
    button.MouseButton1Click:Connect(callback)
    return button
end

local function createTab(parent, text, position, size, color, textColor)
    local tab = Instance.new("TextButton")
    tab.Parent = parent
    tab.Text = text
    tab.Position = position
    tab.Size = size
    tab.BackgroundColor3 = color
    tab.TextColor3 = textColor
    createUICorner(tab, 15)
    return tab
end

local function animateFrame(frame, targetPosition)
    local tweenInfo = TweenInfo.new(0.5, Enum.EasingStyle.Quad, Enum.EasingDirection.InOut)
    local tweenGoal = {Position = targetPosition}
    local tween = TweenService:Create(frame, tweenInfo, tweenGoal)
    tween:Play()
end

local ScreenGui = Instance.new("ScreenGui")
local MainFrame = Instance.new("Frame")
local TabFrame = Instance.new("Frame")
local ContentFrame = Instance.new("Frame")
local CurrentTabContent = Instance.new("Frame")  -- Frame for active tab content

ScreenGui.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")
ScreenGui.Name = "APIInterface"

MainFrame.Parent = ScreenGui
MainFrame.BackgroundColor3 = Color3.fromRGB(240, 240, 240)
MainFrame.Position = UDim2.new(0.3, 0, 0.2, 0)
MainFrame.Size = UDim2.new(0.6, 0, 0.7, 0)
createUICorner(MainFrame, 15)

TabFrame.Parent = MainFrame
TabFrame.BackgroundColor3 = Color3.fromRGB(50, 150, 250)
TabFrame.Position = UDim2.new(0, 0, 0, 0)
TabFrame.Size = UDim2.new(0.2, 0, 1, 0)

ContentFrame.Parent = MainFrame
ContentFrame.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
ContentFrame.Position = UDim2.new(0.2, 0, 0, 0)
ContentFrame.Size = UDim2.new(0.8, 0, 1, 0)

-- Create Tab Buttons
local function createTabButtons()
    local buttons = {}
    
    table.insert(buttons, createTab(TabFrame, "Universal Exploit Functions", UDim2.new(0, 0, 0, 0), UDim2.new(1, 0, 0.1, 0), Color3.fromRGB(30, 130, 200), Color3.fromRGB(255, 255, 255)))
    table.insert(buttons, createTab(TabFrame, "Settings", UDim2.new(0, 0, 0.1, 0), UDim2.new(1, 0, 0.1, 0), Color3.fromRGB(30, 130, 200), Color3.fromRGB(255, 255, 255)))
    table.insert(buttons, createTab(TabFrame, "Trolling", UDim2.new(0, 0, 0.2, 0), UDim2.new(1, 0, 0.1, 0), Color3.fromRGB(30, 130, 200), Color3.fromRGB(255, 255, 255)))
    table.insert(buttons, createTab(TabFrame, "Annoy Players", UDim2.new(0, 0, 0.3, 0), UDim2.new(1, 0, 0.1, 0), Color3.fromRGB(30, 130, 200), Color3.fromRGB(255, 255, 255)))
    table.insert(buttons, createTab(TabFrame, "CRAZY FUNCTIONS", UDim2.new(0, 0, 0.4, 0), UDim2.new(1, 0, 0.1, 0), Color3.fromRGB(30, 130, 200), Color3.fromRGB(255, 255, 255)))

    -- Handle button click for tab switching
    for _, button in ipairs(buttons) do
        button.MouseButton1Click:Connect(function()
            -- Remove previous tab content
            if CurrentTabContent.Parent then
                CurrentTabContent:Destroy()
            end
            
            -- Create new content based on selected tab
            CurrentTabContent = Instance.new("Frame")
            CurrentTabContent.Parent = ContentFrame
            CurrentTabContent.Size = UDim2.new(1, 0, 1, 0)
            CurrentTabContent.BackgroundColor3 = Color3.fromRGB(255, 255, 255)

            -- Handle content for each tab
            if button.Text == "Universal Exploit Functions" then
                createExploitFunctions(CurrentTabContent)
            elseif button.Text == "Settings" then
                createSettings(CurrentTabContent)
            elseif button.Text == "Trolling" then
                createTrolling(CurrentTabContent)
            elseif button.Text == "Annoy Players" then
                createAnnoyPlayers(CurrentTabContent)
            elseif button.Text == "CRAZY FUNCTIONS" then
                createCrazyFunctions(CurrentTabContent)
            end
        end)
    end
end

-- Universal Exploit Functions Content
local function createExploitFunctions(parent)
    local espButton = createButton(parent, "ESP", UDim2.new(0.1, 0, 0.1, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(100, 100, 255), Color3.fromRGB(255, 255, 255), function()
        -- ESP Script
        local players = game:GetService("Players")
        for _, player in ipairs(players:GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("Head") then
                local espBox = Instance.new("BoxHandleAdornment")
                espBox.Adornee = player.Character.Head
                espBox.Size = Vector3.new(2, 2, 2)
                espBox.Color3 = Color3.fromRGB(255, 0, 0)
                espBox.Transparency = 0.5
                espBox.Parent = workspace
            end
        end
        print("ESP Activated")
    end)

    local noclipButton = createButton(parent, "Noclip", UDim2.new(0.1, 0, 0.2, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(100, 100, 255), Color3.fromRGB(255, 255, 255), function()
        -- Noclip Script
        local player = game.Players.LocalPlayer
        local character = player.Character
        if character then
            local humanoid = character:FindFirstChildOfClass("Humanoid")
            if humanoid then
                humanoid.PlatformStand = true
                for _, part in pairs(character:GetChildren()) do
                    if part:IsA("BasePart") then
                        part.CanCollide = false
                    end
                end
            end
        end
        print("Noclip Activated")
    end)

    -- More functions (Fly, Aimbot, etc.)
end

-- Settings Content
local function createSettings(parent)
    local label = Instance.new("TextLabel")
    label.Parent = parent
    label.Text = "Настройки интерфейса"
    label.Position = UDim2.new(0.1, 0, 0.1, 0)
    label.Size = UDim2.new(0.8, 0, 0.1, 0)
    label.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
    label.TextColor3 = Color3.fromRGB(0, 0, 0)
    createUICorner(label, 15)

    -- Example: Toggle Button for Anti-AFK
    local antiAFKButton = createButton(parent, "Anti AFK", UDim2.new(0.1, 0, 0.2, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(100, 255, 100), Color3.fromRGB(255, 255, 255), function()
        -- Anti AFK Script
        game:GetService("Players").LocalPlayer.Idled:Connect(function()
            game:GetService("VirtualUser"):Button2Down(Vector2.new(0, 0), game:GetService("Players").LocalPlayer)
            game:GetService("VirtualUser"):Button2Up(Vector2.new(0, 0), game:GetService("Players").LocalPlayer)
        end)
        print("Anti AFK Activated")
    end)
end

-- Trolling Content
local function createTrolling(parent)
    local flingButton = createButton(parent, "Fling All", UDim2.new(0.1, 0, 0.1, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(255, 100, 100), Color3.fromRGB(255, 255, 255), function()
        -- Fling All Script
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
                player.Character.HumanoidRootPart.CFrame = CFrame.new(math.random(-100, 100), 50, math.random(-100, 100))
            end
        end
        print("Fling All Activated")
    end)
end

-- Annoy Players Content
local function createAnnoyPlayers(parent)
    local bringButton = createButton(parent, "Bring All", UDim2.new(0.1, 0, 0.1, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(255, 100, 100), Color3.fromRGB(255, 255, 255), function()
        -- Bring All Script
        for _, player in pairs(game:GetService("Players"):GetPlayers()) do
            if player.Character and player.Character:FindFirstChild("HumanoidRootPart") then
                player.Character.HumanoidRootPart.CFrame = game.Players.LocalPlayer.Character.HumanoidRootPart.CFrame
            end
        end
        print("Bring All Activated")
    end)
end

-- CRAZY FUNCTIONS Content
local function createCrazyFunctions(parent)
    local crashButton = createButton(parent, "Crash Server", UDim2.new(0.1, 0, 0.1, 0), UDim2.new(0.8, 0, 0.1, 0), Color3.fromRGB(255, 50, 50), Color3.fromRGB(255, 255, 255), function()
        -- Crash Server Script (Simulated)
        while true do
            local newPart = Instance.new("Part")
            newPart.Size = Vector3.new(100, 100, 100)
            newPart.Anchored = true
            newPart.Position = Vector3.new(math.random(-1000, 1000), math.random(50, 200), math.random(-1000, 1000))
            newPart.Parent = workspace
        end
        print("Server Crash Activated")
    end)
end

-- Initial setup
createTabButtons()
