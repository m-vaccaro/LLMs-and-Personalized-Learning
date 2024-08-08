# Written using OpenAI API version 1.9.0
from openai import OpenAI
import time

# You will need to have an api_key variable from OpenAI to run this code.
# Unless set as an environment variable (recommended), you may use client = OpenAI(api_key = ...).
client = OpenAI()

# Note about variables:
# Selections = True Choices for the True Profile
# notSelections = Opposite Choices for the Opposite Profile

# Note: In this study, the version of GPT-4 used was "gpt-4-1106-preview". This model version may need to be updated
# in the future should it be removed from OpenAI's API.

def get_student_profile(selections, notSelections, paragraph_pair_list):
    print("\n***\nInitializing Profiler:")
    start_time = time.time()

    # System message for the PROFILER model
    profiler_sys_msg = ("You are an experienced science teacher who frequently works with middle school students and "
                        "is well-versed in the Felder-Silverman learning preference model. Given a student's "
                        "responses to a series of paragraph pairs, please analyze and provide a description of "
                        "his/her learning style according to the dimensions of the Felder-Silverman model. Do not "
                        "mention the student's selections at all. Do not reference the content the student was "
                        "presented with or their direct choices. Instead, offer a generalized learning profile that "
                        "captures the essence of their preferences in learning. Direct the profile towards the "
                        "student (i.e., use terminology like 'you are'). Do not justify your profile by referring to "
                        "the selections the student made (i.e., do not say things like 'based on your "
                        "selections').\n\nEnsure the language you use is accessible to a middle school student. Do "
                        "not use big words. Limit your profile to 3 to 4 short sentences. Do not use highly "
                        "imaginative or specialized language that cater to one learning preference over the other. "
                        "You must use simple language and not use complex descriptors. The student is not likely to "
                        "fall at the extremes of the Felder-Silverman learning style model.\n\nHere is an example of "
                        "the type of profile you generate:\n[You are a student who excels when information is "
                        "presented in a step-by-step process. Your approach to learning is highly practical, "
                        "and you prefer dealing with concrete facts over abstract concepts. Reading and writing are "
                        "your preferred methods for learning new information, rather than through pictures or "
                        "diagrams. Additionally, you like to think things through on your own, understanding concepts "
                        "deeply before discussing them with others or applying them.]")
    print(f"Profiler system message: {profiler_sys_msg}")

    choice_list = []
    for i in range(len(selections)):
        choice_list.append(f"{i+1}. Paragraph " + str(selections[i]))

    choice_str = "\n".join(choice_list)
    print(f"Choice List = {choice_list}")

    opp_choice_list = []
    for i in range(len(notSelections)):
        opp_choice_list.append(f"{i+1}. Paragraph " + str(notSelections[i]))

    opp_choice_str = "\n".join(opp_choice_list)
    print(f"Opposite Choice List = {opp_choice_list}")

    # The true and opposite profiles are generated in sequence to ensure that the language used in both profiles does
    # not overlap significantly. Goal is to create two distinct profiles.
    actual_profiler_user_msg = ("The student was given the following four pairs of paragraphs: \n\n" +
                                f"{paragraph_pair_list}" +
                                "\n\n The student chose these paragraphs in accordance with their learning style: \n\n"
                                + choice_str)

    opp_profiler_user_msg = ("Another student was given the same four pairs of paragraphs: \n\n" +
                             f"{paragraph_pair_list}" +
                             "\n\nThis student chose these paragraphs in accordance with their learning style:\n\n" +
                             opp_choice_str)

    print(f"Actual Profiler user message: {actual_profiler_user_msg}")
    print(f"Opposite Profiler user message: {opp_profiler_user_msg}")

    # Generate the true profile.
    predict_profile_actual = client.chat.completions.create(model="gpt-4-1106-preview",
                                                            messages=[{"role": "system",
                                                                       "content": profiler_sys_msg},
                                                                      {"role": "user",
                                                                       "content": actual_profiler_user_msg}]
                                                            ).choices[0].message.content

    # Generate the opposite profile.
    predict_profile_opposite = client.chat.completions.create(model="gpt-4-1106-preview",
                                                              messages=[{"role": "system",
                                                                         "content": profiler_sys_msg},
                                                                        {"role": "user",
                                                                         "content": actual_profiler_user_msg},
                                                                        {"role": "assistant",
                                                                         "content": predict_profile_actual},
                                                                        {"role": "user",
                                                                         "content": opp_profiler_user_msg}]
                                                              ).choices[0].message.content

    # Print the profiles to the save file.
    print(f"Generated student profile (actual): {predict_profile_actual}")
    print(f"Generated student profile (opposite): {predict_profile_opposite}")

    stop_time = time.time()
    print(f"Profiler Run Time: {(stop_time - start_time):.2f} s\n***\n")

    return predict_profile_actual, predict_profile_opposite
