# Written using OpenAI API version 1.9.0
from openai import OpenAI
import random
import time

# You will need to have an api_key variable from OpenAI to run this code.
# Unless set as an environment variable (recommended), you may use client = OpenAI(api_key = ...).
client = OpenAI()

# Note: The GUI gives
def get_gpt_response(student_profile, interaction_num):
    print("\n***\nInitializing Rewrite Bot:")
    start_time = time.time()

    # These are the original texts retrieved from Wikipedia, used as input to the GUI.
    # References for original_texts (provided as weblinks to the stable versions of the Wikipedia pages):
    # Plate Tectonics - https://en.wikipedia.org/w/index.php?title=Plate_tectonics&oldid=1191104944
    # Electricity - https://en.wikipedia.org/w/index.php?title=Electricity&oldid=1191110291
    original_texts = ["Earth's lithosphere, the rigid outer shell of the planet including the crust and upper mantle, "
                      "is fractured into seven or eight major plates (depending on how they are defined) and many "
                      "minor plates or 'platelets'. Where the plates meet, their relative motion determines the type "
                      "of plate boundary (or fault): convergent, divergent, or transform. Faults tend to be "
                      "geologically active, experiencing earthquakes, volcanic activity, mountain-building, and "
                      "oceanic trench formation.",
                      "The movement of electric charge is known as an electric current, the intensity of which is "
                      "usually measured in amperes. Electric current can flow through some things, electrical "
                      "conductors, but will not flow through an electrical insulator. By historical convention, "
                      "a positive current is defined as having the same direction of flow as any positive charge it "
                      "contains, or to flow from the most positive part of a circuit to the most negative part. "
                      "Current defined in this manner is called conventional current."]

    # These generic rewrites were produced previously from the original_texts above by GPT-4.
    generic_rewrites = ["The Earth's lithosphere, composed of the crust and part of the mantle, is segmented into "
                        "seven or eight principal plates and numerous smaller ones. These plates intersect at "
                        "boundaries where their movement relative to each other characterizes the boundary type: "
                        "convergent, divergent, or transform. Boundaries where plates interact are often sites of "
                        "geological activity, such as earthquakes, volcanism, the creation of mountains, and the "
                        "development of oceanic trenches.",
                        "Electric current refers to the flow of electric charge, typically measured in amperes. "
                        "Certain materials, known as electrical conductors, allow the passage of electric current, "
                        "whereas electrical insulators do not support such flow. Traditionally, positive current is "
                        "described as moving in the same direction as any contained positive charge or from the "
                        "positive to the negative end of a circuit. This type of current is known as conventional "
                        "current."]

    # System message for the REWRITE model
    rewrite_system = ("You are an experienced middle school science teacher who is capable of reworking scientific "
                      "texts for diverse middle school students. Your writing style is simple. You will be shown a "
                      "profile that has been written to describe a student's learning preferences on the "
                      "Felder-Silverman learning style dimensions. The profile is addressing the student. You will "
                      "also be shown a paragraph describing a middle school science concept. Your task is to rework "
                      "the given paragraph so that it caters to the student's preferences for learning and textual "
                      "presentation. At the same time, you must aim for a balance between engaging and "
                      "straightforward explanations and ensure the scientific content remains clear and accessible. "
                      "Do not use of highly imaginative, specialized language or key words (such as 'imagine') that "
                      "cater to one learning preference over the others. The goal is to make the concept "
                      "understandable and interesting to a student who generally fits the given description.\n\nYour "
                      "reworked paragraph must be approximately the same length as the provided paragraph. Your "
                      "rework must be one short paragraph that is less than one hundred words long. In addition, "
                      "the rework you provide must use language that is appropriate for a middle school student "
                      "(i.e., do not use big words) and must remain academic in tone. Do not mention the student's "
                      "profile, simply provide your rework.")

    print(f"Rewrite Bot System Message: {rewrite_system}")

    rewrite_user_msg = f"The student profile is as follows:\n[{student_profile}]\n\n"
    rewrite_user_msg += (f"Here is the paragraph you need to "
                         f"rework for the student:\n[{original_texts[interaction_num - 1]}]")
    print("Original wikipedia text GPT rewrote this time: " + original_texts[interaction_num - 1])
    print("Generic GPT Rewrite text: " + generic_rewrites[interaction_num - 1])
    print(f"Rewrite Bot User Message: {rewrite_user_msg}")

    generation = client.chat.completions.create(model="gpt-4-1106-preview",
                                                messages=[{"role": "system",
                                                           "content": rewrite_system},
                                                          {"role": "user",
                                                           "content": rewrite_user_msg}]
                                                ).choices[0].message.content
    print(f"Rewritten Paragraph for GPT interaction {interaction_num}: {generation}")

    # Present the original vs rewritten paragraph in a random order, but save that order so we know for data analysis.
    possibilities = ['first', 'second']  # Defines the possibilities for position of original text.
    choice = random.choice(possibilities)

    if choice == 'first':
        paragraph1 = generic_rewrites[interaction_num - 1]
        paragraph2 = generation
        order = "Generic rewrite first, customized rewrite second."
    else:
        paragraph1 = generation
        paragraph2 = generic_rewrites[interaction_num - 1]
        order = "Customized rewrite first, generic rewrite second."
    print(choice + "  --->  " + order)

    stop_time = time.time()
    print(f"Rewrite Run Time: {(stop_time - start_time):.2f} s\n***")

    return paragraph1, paragraph2
