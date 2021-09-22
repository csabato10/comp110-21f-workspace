"""Under the Influence"""

import random
points: int = 0
player: str = ""
bio: str = ""
NAMED_CONSTANT: str = "\U0001F4F8"


def adventurous():
    print("Ooooo I bet you think you're quirky and cool for saying you're adventurous.")
    global bio
    global points
    bio = bio + input("Write a fun bio that doesn't make you sound like a wet blanket: ")
    print("Your new bio says: " + bio)
    if len(bio) <= 200:
        points += 15
    elif len(bio) <= 100:
        points += 30
    else:
        points += 10
    print("I bet you think you're a crackhead because you've gone skateboarding one time. Whatever, be who you want.\nLet's post your first picture on Insta.")
    adventure_picture()


def adventure_picture():
    global points
    pic_one: int = int(input("What type of picture do you want to post?\n1. Beach picture\n2. Cool car picture\n3. Night club picture\n4. Cliff diving picture\n5. Haunted house picture\nOption number: "))
    filter_on_image: str = input("Do you want to put a filter on this picture? Y or N: ").upper()
    if pic_one == 1 and filter_on_image == "Y":
        points += 300
    elif pic_one == 1 and filter_on_image == "N":
        points += 200
    elif pic_one == 2 and filter_on_image == "Y":
        points += 150
    elif pic_one == 2 and filter_on_image == "N":
        points += 100
    elif pic_one == 3 and filter_on_image == "Y":
        points += 200
    elif pic_one == 3 and filter_on_image == "N":
        points += 175
    elif pic_one == 4 and filter_on_image == "Y":
        points += 470
    elif pic_one == 4 and filter_on_image == "N":
        points += 400
    elif pic_one == 5 and filter_on_image == "Y":
        points += 100
    elif pic_one == 5 and filter_on_image == "N":
        points += 75
    else:
        print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")


def confidence():
    print("I bet you think your confidence is attractive. The followers will determine that.")
    global bio
    global points
    bio = bio + input("Write a fun bio that makes you seem confident. Try to not be conceited about it though, you're not Kanye, it won't work for you: ")
    print("Your new bio says: " + bio)
    if len(bio) <= 200:
        points += 15
    elif len(bio) <= 100:
        points += 30
    else:
        points += 10
    print("Since you think you're so cool. What kind of picture do you want to post first hot stuff?")
    confident_picture()


def confident_picture():
    global points
    pic_one: int = int(input("What type of picture do you want to post?\n1. Bathing suit picture\n2. Sunglasses picture\n3. Golden hour picture\n4. Modeling picture\n5. Picture with friends\nOption number: "))
    if pic_one == 1:
        points += 200
    elif pic_one == 2:
        points += 100
    elif pic_one == 3:
        points += 175
    elif pic_one == 4:
        points += 300
    elif pic_one == 5:
        points += 250
    else:
        print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")
    print("You currently have", points, "followers.")


def vulnerable():
    print("Boring. Whatever. Do what you want I guess.")
    global bio
    global points
    bio = bio + input("Write a fun bio that makes you seem...idk...relatable? Is that what you're going for: ")
    print("Your new bio says: " + bio)
    if len(bio) <= 200:
        points += 15
    elif len(bio) <= 100:
        points += 30
    else:
        points += 10
    print("Time for a picture that makes you look soooo deep and emotional.")
    vulnerable_picture()


def vulnerable_picture():
    global points
    pic_one: int = int(input("What type of picture do you want to post?\n1. Picture of you with a dog\n2. A picture of a cup of coffee on a cold day\n3. Sunset picture\n4. Movie on the couch picture\n5. Picture with a significant other\nOption number: "))
    if pic_one == 1:
        points += 300
        print("Great post. People love animals.")
    elif pic_one == 2:
        points += 25
    elif pic_one == 3:
        points += 50
    elif pic_one == 4:
        points += 80
    elif pic_one == 5:
        points += 40
    else:
        print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")
    print("You currently have", points, "followers.")


def tiktok() -> str:
    global points
    print("I have no idea why you want to become a TikTok influencer too because I can tell that you don't know how to dance and are not that funny either.")
    vid_type: int = int(input("What kind of TikTok do you want to make?\n1. Dance video\n2. Duet a famous TikToker\n3. Tell a funny joke/story\nOption number: "))
    print("The TikTok algorthim is weird so don't expect too much " + player + ".")
    if vid_type == 1:
        points += random.randint(50, points + 500)
    elif vid_type == 2:
        points += random.randint(90, points + 300)
    elif vid_type == 3:
        points += random.randint(0, points + 400)
    else:
        print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")
    return str(random.randint(0, 5)) + " people dueted or stitched your most recent TikTok."


def insta():
    global points
    picture: int = int(input("What kind of vibe do you want your Insta post to have?\n1. Adventurous\n2. Cool\n3. Casual\nChoice number: "))
    if picture == 1:
        adventure_picture()
    elif picture == 2:
        confident_picture()
    elif picture == 3:
        vulnerable_picture()
    else:
        print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")


def twitter() -> str:
    global player
    global points
    tweet: str = input("What stupid thing do you want to post now that you feel like everyone needs to read?\n" + player + ": ")
    while True:
        if len(tweet) >= 280:
            print("Your tweet is too long")
        else:
            i: int = 0
            tag_count: int = 0
            while i < len(tweet):
                if tweet[i] == "#":
                    tag_count += 1
                i += 1
            
            if tag_count >= 1:
                if len(tweet) < 100:
                    points += random.randint(100, points + 200)
                    break
                else:
                    points += random.randint(0, points)
                    break
            else:
                points += random.randint(0, 500)
                break
    return "On top of likes, you received " + str(random.randint(0, 100)) + " retweets on that tweet."
                

def biography():
    global points
    print("Time to decide what kind of online persona do you want to create for yourself")
    profile: int = int(input('If you change your mind and decide being an influencer is no longer the journey for you, just type in 4: \n 1. Adventurous and badass \U0001F919\U0001F609 \n 2. Confident and cool \U0001F61D \n 3. Cute and casual \U0001F499\nInfluencer type: '))
    if profile == 4:
        print("Lame. You ended with " + str(points) + " followers.")
    elif profile == 1:
        adventurous()
    elif profile == 2:
        confidence()
    elif profile == 3:
        vulnerable()
        

def greet() -> None:
    print("Sup loser. Welcome to Under the Influence, the fastest way to become a social media icon.")
    global player
    player = "@" + input("What is your username? ")
    print(player + " is such a lame username. It's too late to change it though so I guess you're stuck with it.")
    print("I'm Tiffany, I'll be your guide through your journey in becoming a social media influencer. \nYou're going to have a bunch of opportunities to post on various platforms. \nBut first...we need to get your profile together.")


def certified(player: str) -> str:
    print("Alright, it's time to see if you were able to get certified on social media. You know...that check mark that means you're officially cool.")
    i: int = 1
    while i <= 10:
        print("\U0001F941" * i)
        i += 1
    player = player + "\U00002705"
    return player
    

def profile_pic(points: int) -> int:
    print("First step, aside from your username duh, is creating a profile picture.")
    while True:
        ppf_type: int = int(input("What type of picture do you want?\n1. Black and white solo picture\n2. Picture centered on you with other people present\n3. Picture of you and an animal\n4. Picture of something random\nProfile picture type: "))
        print("Just so you know, " + player + ", if people don't know what you look like, they probably won't want to follow you.")
        ppf_confirmation: str = input("That being said, do you want to change you previous choice? Y or N: ").upper()
        if ppf_confirmation == "Y":
            continue
        else:
            if ppf_type == 1 or 2:
                points += 70
            elif ppf_type == 3:
                points += 100
            else:
                points += 8
        return points


def main():
    greet()
    print(f"Your profile picture earned you {profile_pic(points)} new followers. Before you get too excited, I'm sure one of those people is your mom, you're not famous yet.")
    biography()
    while True:
        influencer_loop: str = input("Where would you like to post next? Insta, Tiktok, or Twitter? If you think you've received enough followers to be certified on each account, type 'quit': ").lower()
        if influencer_loop == "insta":
            insta()
        elif influencer_loop == "tiktok":
            print(tiktok())
        elif influencer_loop == "twitter":
            print(twitter())
        elif influencer_loop == "quit":
            break
        else:
            print("You really need to get better with technology if you want to become and influencer because I have no idea what you just said.")
            print("Try again to tell me what you want to do.")
        print("Your follower count is now: " + str(points))
        print(NAMED_CONSTANT)
    if points >= 10_000:
        print(f"Influencer status: {certified(player)}")
        print("Wow, I really didn't think you could do it. Congrats, I'm honestly impressed.\nThanks for choosing Under the Influence for your journey to fame.\nTiff out.")
    else:
        print("Influencer status: " + player + ". Awww. You really hate to see it. Good try at least? Maybe in a different life? It was definitely worth a shot, you're just not the right type for this.\nTiff out.")


if __name__ == "__main__":
    main()
