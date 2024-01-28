from player import player


def communication_0() -> tuple[str, bool]:
    message = ["Hallo user, ich bin Dein persönlicher Assistent.", "Verrätst Du mir Deinen Vornamen? (j/n)"]
    new_input = True
    next_message = 1
    return message, new_input, next_message


def communication_1(input_text: str) -> tuple[str, bool, int]:
    if input_text == "j":
        message = ["Vielen Dank! Bitte gib Deinen Vornamen in das Textfeld ein.", ""]
        new_input = True
        next_message = 2
    elif input_text == "n":
        message = ['Das kann ich gut verstehen.', 'Ich werde Dich einfach "user" nennen.', 'mit Return bestätigen']
        player.name = "User"
        new_input = True
        next_message = 2
    else:
        message = ["Ich habe Dich nicht verstanden.", "Bitte antworte mit 'j' oder 'n'."]
        new_input = True
        next_message = 1

    return (message, new_input, next_message)


def communication_2(player_name: str) -> tuple[str, bool]:
    if player.name != "User":
        player.name = player_name.strip().capitalize()
    if player.name == "User":
        message = [
            "Wie möchtest Du angesprochen werden: ",
            "1) Liebe Userin, 2) Lieber User oder 3) Liebes User",
        ]
    else:
        message = [
            f"{player.name} ist ein sehr schöner Name!",
            "Er erinnert mich an jemanden den ich vor langer Zeit gekannt habe, Wie möchtest",
            f"Du angesprochen werden? A) Liebe, B) Lieber oder C) Liebes {player.name}",
        ]
    next_message = 3
    new_input = True
    return message, new_input, next_message


def communication_3(gender: str) -> tuple[str, bool, int]:
    new_input = True
    next_message = None
    return_text = "Drücke Return, um das Spiel zu starten"
    if gender == "a" or gender == "1":
        player.sex = "female"
        message = [f"Alles klar liebe {player.name}. {return_text}"]
        next_message = 4
        if gender == "1":
            player.name = "Userin"
    elif gender == "b" or gender == "2":
        player.sex = "male"
        message = [f"Alles klar lieber {player.name}. {return_text}"]
        next_message = 4
    elif gender == "c" or gender == "3":
        player.sex = "divers"
        message = [f"Alles klar liebes {player.name}. {return_text}"]
        next_message = 4
    else:
        message = [f"Gib A für Liebe {player.name}, B für Lieber {player.name}", f"oder C für Liebes {player.name} ein."]
        next_message = 3
        new_input = True


    return message, new_input, next_message


def communication_4(input):
    new_input = False
    next_message = None
    message = [
        "Du kannst zweimal neu würfeln.",
        "Klicke auf einen Würfel, um in zu sperren oder freizugeben",
        "Wenn Du den Wurf behalten möchtest, klicke auf 'OK'",
    ]

    return message, new_input, next_message


def create_message(input_text: str, communication_counter: int) -> tuple[str, bool]:
    text = input_text.strip().lower()
    # Begrüßung
    if communication_counter == 0:
        message, new_input, next_message = communication_0()
    # Namen eingeben ja/nein
    if communication_counter == 1:
        message, new_input, next_message = communication_1(text)
    # Abfrage Name oder "user"
    if communication_counter == 2:
        message, new_input, next_message = communication_2(text)
    # Abfrage gender
    if communication_counter == 3:
        message, new_input, next_message = communication_3(text)
    if communication_counter == 4:
        message, new_input, next_message = communication_4(text)

    return message, new_input, next_message
