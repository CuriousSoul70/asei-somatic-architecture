# TouchDesigner Python Script (CHOP Execute DAT)
# Listens for OSC messages from the Edge Broker to switch visual environments[cite: 2].

def onReceiveOSC(dat, rowIndex, message, bytes, timeStamp, peer):
    scene_target = message[0]
    
    # Map the Affective Engine's output to TouchDesigner MovieFileIn TOPs
    if scene_target == "Deep Misty Glade":
        op('crossfade1').par.cross = 0.0 # Fade to Video 1[cite: 2]
    elif scene_target == "Alpine Waterfall":
        op('crossfade1').par.cross = 1.0 # Fade to Video 2[cite: 2]
    elif scene_target == "Sunlit Bamboo":
        op('crossfade1').par.cross = 2.0 # Fade to Video 3[cite: 2]
    else:
        op('crossfade1').par.cross = 3.0 # Default / Golden Hour[cite: 2]
        
    print(f"ASEI Visual Engine: Transitioning to {scene_target}")
    return
