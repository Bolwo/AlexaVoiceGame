import urllib2
import json
import Player

def lambda_handler(event, context):
    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])

def on_session_started(session_started_request, session):
    print "Starting new session."
    
def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...
    
def on_launch(launch_request, session):
    return get_welcome_response()
    
def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]
    
    if intent_name == "StartGame":
        return startgame(session)
    if intent_name == "EndGame":
        return endgame(session)
    if intent_name == "SaveGame":
        return savegame(session)
    if intent_name == "Move":
        return move(session)
    if intent_name == "Pickup":
        return pickup(session)
    if intent_name == "Inventory":
        return inventory(session)
    if intent_name == "Description":
        return description(session)
    else:
        raise ValueError("Invalid intent")



def get_welcome_response():
    p = Player.Player("Welcome room", ['exampleroomitem'], [])
    card_title = "Ship"
    speech_output = str(p.room.description) + ". In the corner you see "
    for i in p.room.items:
        speech_output += i.name
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = {"RoomDescription": p.room.description,
        "RoomItems": json.dumps(p.room.items, default=lambda x: x.name),
        "PlayerItems": json.dumps(p.items, default=lambda x: x.name)
    }
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
        
def startgame():
    session_attributes = {}
    card_title = "start"
    speech_output = "New game started. As the computer, I control the ship. Luckily for you I am programmed to abide by your every command." \
                    "Tell me where to go by saying 'Go North', for example"
    reprompt_text = "I didn't get that."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def move(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    #p = Player.Player('testroom', ["testroomitem"], ['testplayeritem'])
    p.move()
    session_attributes = {}
    card_title = "move"
    speech_output = "The room is " + str(p.room.description) + ". In the corner you see "
    for i in p.room.items:
        speech_output += i.name
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
     
def pickup(session):
    #p = Player.Player("Welcome room", ['exampleroomitem'], ['exampleplayeritem'])
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    p.pickup()
    card_title = "pickup"
    speech_output = "You picked up the items"
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
     
def inventory(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    card_title = "pickup"
    speech_output = "In your inventory you have "
    for i in p.items:
        speech_output += i.name + ", "
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def endgame(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    card_title = "end"
    speech_output = "Game ended"
    reprompt_text = "I didn't get that."
    should_end_session = True
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def savegame(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    card_title = "save"
    speech_output = "Game saved. (not really though as I am not able to do that yet)"
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def description(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    card_title = "description"
    speech_output = "The room is " + str(p.room.description) + ". In the corner you see "
    for i in p.room.items:
        speech_output += i.name
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def help(session):
    p = Player.Player(session['attributes']['RoomDescription'], session['attributes']['RoomItems'], session['attributes']['PlayerItems'])
    card_title = "help"
    speech_output = "To control the ship, the commands are help, move, pickup, description, save game, start game, end game"
    for i in p.room.items:
        speech_output += i.name
    reprompt_text = "I didn't get that."
    should_end_session = False
    session_attributes = save_session(p)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }
        
def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }
    
def save_session(p):
    playeritems = []
    for i in p.items:
        playeritems.append(i.name)
        
    roomitems = []
    for i in p.room.items:
        roomitems.append(i.name)
        
    session_attributes = {"RoomDescription": p.room.description,
        "RoomItems": roomitems,
        "PlayerItems": playeritems
    }
    return session_attributes
