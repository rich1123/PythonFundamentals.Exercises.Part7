from typing import Dict

# # Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: 'English',
    2: 'Spanish',
    3: 'German'
    }
#
# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?',
    2: 'Como te llamas?',
    3: 'Wie heißen sie?'
    }
#
# # Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# # Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: 'Hello ',
    2: 'Hola ',
    3: 'Hallo '
}


def print_language_options(lang_options: Dict[int, str]) -> None:

    #     """
    #     Given a dictionary, this functions iterates through the values and prints them out.
    #
    #     :param lang_options: A dictionary
    #     Keys are integers representing a language id
    #     Values are strings representing the name of a language
    #     :return: None
    #     """
    #     pass  # remove pass statement and implement me
    #
    #     for v in lang_options:
    #         print(lang_options[v])

    print('Please choose a language: ')
    for key, value in lang_options.items():
        print(f'{key}: {value}')
        # print(lang_options[x])


def language_input() -> int:

    #     """
    #     This function prompts the user for a language choice.
    #
    #     :return: An integer representing the language choice made by the user
    #     """
    #     pass  # remove pass statement and implement me
#

    lang_choice = input("type 1 for English, 2 for Spanish, 3 for German\n")

    return int(lang_choice)


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    # """
    # This method determines if the choice the user made is valid.
    #
    # :param lang_options: A dictionary
    # Keys are integers representing a language id
    # Values are strings representing the name of a language
    #
    # :param lang_choice: An integer representing the value the user selected
    # :return: A boolean representing the validity of the lang_choice
    # """
    # pass  # remove pass statement and implement me

    return lang_choice in lang_options

#
# language_choice_is_valid(languages, 1)
# language_choice_is_valid(languages, 4)


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    # """
    # This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding
    # to
    # the lang_choice parameter.
    #
    # :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    # in the users chosen language
    # :param lang_choice: The language the user has chosen
    # :return:
    # """
    # pass  # remove pass statement and implement me
    # name_prompt_dict{}

    name_prompt = name_prompt_options.get(lang_choice)
    return name_prompt
    # return lang_choice

    # print(result)

#
# get_name_input(languages, 1)
# get_name_input(languages, 4)


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

    name = input(name_prompt)
    return name

    # pass  # remove pass statement and implement me

    # for lang_choice in name_prompt_dict.values():
    # for name_prompt in name_prompt_dict
    # return list(name_prompt_dict.keys([list(name_prompt_dict.values()).index(name_prompt)])


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    lang = greetings_options.get(lang_choice)
    print(lang + ' ' + name)

    # pass  # remove pass statement and implement me


if __name__ == '__main__':
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
